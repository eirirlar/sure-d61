<#
.SYNOPSIS
    Convert one or more .emf files to .png using Windows System.Drawing (GDI+).

.DESCRIPTION
    EMF (Enhanced Metafile) is a Windows vector graphics format that most cross-platform
    viewers and Markdown renderers cannot display inline. This script rasterises each
    input .emf to a sibling .png at 2x scale (so line-art stays crisp when the image
    is embedded in a Markdown viewer or a slide).

    The original .emf is left in place — it is the authoritative vector source and can
    be reconverted at any resolution.

.PARAMETER Root
    Directory to scan recursively for .emf files. Defaults to the current directory.

.PARAMETER Scale
    Raster multiplier. Default 2. Increase for print output; decrease if file size matters.

.PARAMETER Force
    Overwrite existing .png sibling files. Off by default.

.EXAMPLE
    powershell -File scripts/emf_to_png.ps1 -Root surewave/images

.NOTES
    Windows-only (uses System.Drawing / GDI+). On Linux/macOS use libreoffice or inkscape instead.
#>

param(
    [string]$Root = ".",
    [int]$Scale = 2,
    [switch]$Force
)

Add-Type -AssemblyName System.Drawing

$emfs = Get-ChildItem -Path $Root -Recurse -Filter *.emf -File
if (-not $emfs) {
    Write-Output "No .emf files found under $Root"
    exit 0
}

$converted = 0
$skipped = 0
$failed = 0

foreach ($emf in $emfs) {
    $png = [System.IO.Path]::ChangeExtension($emf.FullName, ".png")
    if ((Test-Path $png) -and -not $Force) {
        $skipped++
        continue
    }

    try {
        $img = [System.Drawing.Image]::FromFile($emf.FullName)
        $w = [int]($img.Width * $Scale)
        $h = [int]($img.Height * $Scale)
        $bmp = New-Object System.Drawing.Bitmap $w, $h
        $bmp.SetResolution(($img.HorizontalResolution * $Scale), ($img.VerticalResolution * $Scale))
        $g = [System.Drawing.Graphics]::FromImage($bmp)
        $g.SmoothingMode = 'AntiAlias'
        $g.InterpolationMode = 'HighQualityBicubic'
        $g.Clear([System.Drawing.Color]::White)
        $g.DrawImage($img, 0, 0, $w, $h)
        $bmp.Save($png, [System.Drawing.Imaging.ImageFormat]::Png)
        $g.Dispose(); $bmp.Dispose(); $img.Dispose()
        $converted++
    }
    catch {
        Write-Warning ("Failed: " + $emf.FullName + " - " + $_.Exception.Message)
        $failed++
    }
}

Write-Output ("Converted: {0}, Skipped (existing): {1}, Failed: {2}" -f $converted, $skipped, $failed)
