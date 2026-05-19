#!/usr/bin/env python3
"""Chroma-key magenta sprite -> 800x1200 RGBA PNG (+ optional edge feather).

Usage (one file at a time):
  python sprite_chroma_feather.py input_magenta.png lin-wantang-expr-smile-v3
  python sprite_chroma_feather.py input.png lin-wantang-standing --no-feather

Outputs under J:\\项目\\GAL\\美术资源初稿\\立绘\\
  {base}-transparent-v1.png
  {base}-transparent-v1-feather.png   (unless --no-feather)
  backup_gen\\{base}-magenta-v1_rgb.png
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

OUT_DIR = Path(r"J:\项目\GAL\美术资源初稿\立绘")
TARGET_W, TARGET_H = 800, 1200
FEATHER_BLUR = 1.2


def chroma_key_rgba(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    magenta = (r > 140) & (b > 140) & (g < r * 0.75) & (g < b * 0.75)
    magenta |= (r > 180) & (b > 120) & (g < 120) & (r > g + 40)
    dist = np.sqrt((r - 255) ** 2 + g**2 + b**2)
    soft = np.clip((dist - 20) / 50, 0, 1)
    alpha = np.where(magenta, 0, 255 * soft).astype(np.uint8)
    out = np.stack(
        [
            arr[..., 0].astype(np.uint8),
            arr[..., 1].astype(np.uint8),
            arr[..., 2].astype(np.uint8),
            alpha,
        ],
        axis=-1,
    )
    return Image.fromarray(out, "RGBA")


def fit_canvas(im: Image.Image) -> Image.Image:
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    w, h = im.size
    scale = min(TARGET_W / w, TARGET_H / h)
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (TARGET_W, TARGET_H), (0, 0, 0, 0))
    canvas.paste(im, ((TARGET_W - nw) // 2, TARGET_H - nh), im)
    return canvas


def feather_alpha(canvas: Image.Image) -> Image.Image:
    r, g, b, a = canvas.split()
    a_arr = np.array(a, dtype=np.float32)
    a_img = (
        Image.fromarray(a_arr.astype(np.uint8), "L")
        .filter(ImageFilter.MaxFilter(3))
        .filter(ImageFilter.GaussianBlur(radius=FEATHER_BLUR))
    )
    core_arr = np.array(a.filter(ImageFilter.MinFilter(5)), dtype=np.float32) / 255
    edge_arr = np.array(a_img, dtype=np.float32) / 255
    orig_arr = a_arr / 255
    blend = np.clip(np.where(core_arr > 0.92, orig_arr, edge_arr), 0, 1)
    a_out = Image.fromarray((blend * 255).astype(np.uint8), "L")
    return Image.merge("RGBA", (r, g, b, a_out))


def main() -> None:
    p = argparse.ArgumentParser(description="Magenta chroma key + 800x1200 + feather")
    p.add_argument("input", type=Path, help="Magenta-screen PNG (RGB/RGBA)")
    p.add_argument("base_name", help="e.g. lin-wantang-expr-smile-v3")
    p.add_argument("--no-feather", action="store_true")
    args = p.parse_args()

    if not args.input.is_file():
        raise SystemExit(f"Input not found: {args.input}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    bak_dir = OUT_DIR / "backup_gen"
    bak_dir.mkdir(parents=True, exist_ok=True)

    bak = bak_dir / f"{args.base_name}-magenta-v1_rgb.png"
    shutil.copy2(args.input, bak)

    keyed = fit_canvas(chroma_key_rgba(Image.open(args.input)))
    transparent = OUT_DIR / f"{args.base_name}-transparent-v1.png"
    keyed.save(transparent, "PNG")
    print("Wrote", transparent)

    if not args.no_feather:
        feather_path = OUT_DIR / f"{args.base_name}-transparent-v1-feather.png"
        feather_alpha(keyed).save(feather_path, "PNG")
        print("Wrote", feather_path)

    print("Backup", bak)


if __name__ == "__main__":
    main()
