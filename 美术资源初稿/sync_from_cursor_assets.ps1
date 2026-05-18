# 将 Cursor 各临时工程 assets 中的立绘/背景/UI 同步到本目录
$destRoot = $PSScriptRoot
$srcDirs = @(
    "$env:USERPROFILE\.cursor\projects\*\assets"
)
$count = 0
Get-ChildItem -Path $srcDirs -ErrorAction SilentlyContinue | ForEach-Object {
    $src = $_.FullName
    Get-ChildItem $src -Filter '*.png' -File -ErrorAction SilentlyContinue | ForEach-Object {
        $n = $_.Name
        if ($n -match '_original\.png$') { return }
        if ($n -match '^BG_') { $sub = '背景' }
        elseif ($n -match '^UI_') { $sub = 'UI' }
        elseif ($n -match 'lin-wantang|lin_wantang') { $sub = '立绘' }
        else { return }
        $destDir = Join-Path $destRoot $sub
        if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir -Force | Out-Null }
        Copy-Item $_.FullName (Join-Path $destDir $n) -Force
        $count++
    }
}
Write-Host "Synced $count files to $destRoot"
