#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""恢复 UI 基准版：用冻结脚本覆盖当前脚本并重生成粉/蓝全套 PNG。"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

UI = Path(r"J:\项目\GAL\美术资源初稿\UI")
BASELINE = UI / "scripts" / "build_ui_anime_say_baseline.py"
ACTIVE = UI / "scripts" / "build_ui_anime_say.py"


def main() -> None:
    if not BASELINE.is_file():
        raise SystemExit(f"Missing baseline script: {BASELINE}")
    shutil.copy2(BASELINE, ACTIVE)
    print("Restored script:", ACTIVE)
    subprocess.run([sys.executable, str(ACTIVE), "all"], check=True)
    print("Baseline PNGs regenerated. See UI/UI_BASELINE.md")


if __name__ == "__main__":
    main()
