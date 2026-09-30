# Downsample the SUREWAVE D8.3 brochure figures to a screen-brochure DPI.
# Reads originals from `surewave/images/2026-09-28_surewave_d8.3_technical_brochure/`
# and writes reduced-size copies (max 1000 px wide, aspect preserved) to
# `surewave/images/2026-09-28_surewave_d8.3_technical_brochure_lowres/`.
# Originals are not touched. Images already <= max wide are copied through as-is.

param(
    [string]$SrcDir = "C:\dev\src\sure-d61\surewave\images\2026-09-28_surewave_d8.3_technical_brochure",
    [string]$DstDir = "C:\dev\src\sure-d61\surewave\images\2026-09-28_surewave_d8.3_technical_brochure_lowres",
    [int]$MaxWidth = 1000
)

Add-Type -AssemblyName System.Drawing

if (-not (Test-Path $DstDir)) { New-Item -ItemType Directory -Path $DstDir | Out-Null }

$files = Get-ChildItem "$SrcDir\*.png" | Sort-Object Name
$totalIn = 0; $totalOut = 0

foreach ($f in $files) {
    $totalIn += $f.Length
    $img = [System.Drawing.Image]::FromFile($f.FullName)
    $srcW = $img.Width; $srcH = $img.Height
    $dstPath = Join-Path $DstDir $f.Name

    if ($srcW -le $MaxWidth) {
        $img.Dispose()
        Copy-Item -Path $f.FullName -Destination $dstPath -Force
        $outLen = (Get-Item $dstPath).Length
        $totalOut += $outLen
        "{0}  {1,5}x{2,-5} (unchanged, {3:N2} MB)" -f $f.Name, $srcW, $srcH, ($outLen/1MB)
        continue
    }

    $newW = $MaxWidth
    $newH = [int]([math]::Round($srcH * ($MaxWidth / $srcW)))
    $bmp = New-Object System.Drawing.Bitmap $newW, $newH
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
    $g.DrawImage($img, 0, 0, $newW, $newH)
    $g.Dispose()
    $img.Dispose()
    $bmp.Save($dstPath, [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Dispose()
    $outLen = (Get-Item $dstPath).Length
    $totalOut += $outLen
    "{0}  {1,5}x{2,-5} -> {3,4}x{4,-4} ({5:N2} MB -> {6:N2} MB)" -f $f.Name, $srcW, $srcH, $newW, $newH, ($f.Length/1MB), ($outLen/1MB)
}

""
"Total: {0:N2} MB -> {1:N2} MB ({2:N0}% reduction)" -f ($totalIn/1MB), ($totalOut/1MB), (100 * (1 - $totalOut/$totalIn))
