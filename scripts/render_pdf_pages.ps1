[Windows.Data.Pdf.PdfDocument, Windows.Data.Pdf, ContentType = WindowsRuntime] | Out-Null

$pdfFile = Get-Item -LiteralPath (Resolve-Path "public/downloads/Rajasthan_Royals_SupeRR_Selector_Round1_Methodology_Report.pdf")
$doc = [Windows.Data.Pdf.PdfDocument]::LoadFromFileAsync($pdfFile).GetAwaiter().GetResult()
Write-Host "Page Count: $($doc.PageCount)"

$outDir = "public/downloads/pdf_inspection"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }

for ($i = 0; $i -lt $doc.PageCount; $i++) {
    $page = $doc.GetPage($i)
    $dest = "$outDir/page_$($i+1).png"
    if (Test-Path $dest) { Remove-Item $dest }
    $storageFile = [Windows.Storage.StorageFile]::GetFileFromPathAsync((New-Item -ItemType File -Path $dest -Force).FullName).GetAwaiter().GetResult()
    $stream = $storageFile.OpenAsync([Windows.Storage.FileAccessMode]::ReadWrite).GetAwaiter().GetResult()
    $page.RenderToStreamAsync($stream).GetAwaiter().GetResult()
    $stream.FlushAsync().GetAwaiter().GetResult()
    $stream.Dispose()
    $size = (Get-Item $dest).Length
    Write-Host "Rendered page $($i+1): $size bytes"
}
