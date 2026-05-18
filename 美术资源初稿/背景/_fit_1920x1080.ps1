# 等比缩放到 1920x1080 内，留边不裁切
param([string]$Path)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$bak = $Path -replace '\.png$', '_original.png'
if (-not (Test-Path $bak)) { Copy-Item $Path $bak -Force }
$src = if (Test-Path $bak) { $bak } else { $Path }
$tw, $th = 1920, 1080
$img = [System.Drawing.Image]::FromFile($src)
$w, $h = $img.Width, $img.Height
$scale = [Math]::Min($tw / $w, $th / $h)
$nw = [int][Math]::Round($w * $scale)
$nh = [int][Math]::Round($h * $scale)
$out = New-Object System.Drawing.Bitmap $tw, $th
$g = [System.Drawing.Graphics]::FromImage($out)
$g.Clear([System.Drawing.Color]::FromArgb(28, 22, 18))
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$x = [int](($tw - $nw) / 2)
$y = [int](($th - $nh) / 2)
$g.DrawImage($img, $x, $y, $nw, $nh)
$g.Dispose(); $img.Dispose()
$out.Save($Path, [System.Drawing.Imaging.ImageFormat]::Png)
$out.Dispose()
$v = [System.Drawing.Image]::FromFile($Path)
Write-Output "${w}x${h} -> $($v.Width)x$($v.Height) letterbox"
$v.Dispose()
