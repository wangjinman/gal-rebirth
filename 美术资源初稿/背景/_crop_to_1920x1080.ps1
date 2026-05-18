param([string]$Path)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$bak = $Path -replace '\.png$', '_original.png'
if (-not (Test-Path $bak)) { Copy-Item $Path $bak -Force }
$tw, $th = 1920, 1080
$img = [System.Drawing.Image]::FromFile($bak)
$w, $h = $img.Width, $img.Height
$scale = [Math]::Max($tw / $w, $th / $h)
$nw = [int][Math]::Round($w * $scale)
$nh = [int][Math]::Round($h * $scale)
$bmp = New-Object System.Drawing.Bitmap $nw, $nh
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.DrawImage($img, 0, 0, $nw, $nh)
$g.Dispose(); $img.Dispose()
$left = [int](($nw - $tw) / 2); $top = [int](($nh - $th) / 2)
$out = New-Object System.Drawing.Bitmap $tw, $th
$g2 = [System.Drawing.Graphics]::FromImage($out)
$destRect = New-Object System.Drawing.Rectangle -ArgumentList 0, 0, $tw, $th
$srcRect = New-Object System.Drawing.Rectangle -ArgumentList $left, $top, $tw, $th
$g2.DrawImage($bmp, $destRect, $srcRect, [System.Drawing.GraphicsUnit]::Pixel)
$g2.Dispose(); $bmp.Dispose()
$out.Save($Path, [System.Drawing.Imaging.ImageFormat]::Png)
$out.Dispose()
$v = [System.Drawing.Image]::FromFile($Path)
Write-Output "$w x $h -> $($v.Width)x$($v.Height)"
$v.Dispose()
