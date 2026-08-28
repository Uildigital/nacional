$dirs = Get-ChildItem -Path "." -Directory
foreach ($dir in $dirs) {
    $file = Join-Path $dir.FullName "index.html"
    if (Test-Path $file) {
        $content = Get-Content $file -Raw
        if ($content -notmatch "_vercel/insights/script.js") {
            $content = $content -replace "</head>", "<script defer src=`"/_vercel/insights/script.js`"></script>`r`n</head>"
            Set-Content -Path $file -Value $content -NoNewline
            Write-Host "Updated $file"
        }
    }
}
Write-Host "Done"
