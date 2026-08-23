$results = @()
$dirs = Get-ChildItem -Path "." -Directory
foreach ($dir in $dirs) {
    $file = Join-Path $dir.FullName "index.html"
    if (Test-Path $file) {
        $content = Get-Content $file -Raw
        $titleMatch = [regex]::match($content, '(?si)<h1.*?>(.*?)</h1>')
        $linkMatch = [regex]::match($content, '(?si)<a href="([^"]+)"[^>]*class="modal-btn"')
        $title = if ($titleMatch.Success) { ($titleMatch.Groups[1].Value -replace '<[^>]+>','').Trim() } else { "N/A" }
        $link = if ($linkMatch.Success) { $linkMatch.Groups[1].Value } else { "N/A" }
        
        $results += [PSCustomObject]@{ Folder=$dir.Name; Title=$title; Link=$link }
    }
}
$results | ConvertTo-Json
