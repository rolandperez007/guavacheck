$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"

$destination = ".\developer\backup\guavacheck-$timestamp.zip"

Compress-Archive `
    -Path * `
    -DestinationPath $destination `
    -CompressionLevel Optimal `
    -Force

Write-Host ""
Write-Host "Project backup created:"
Write-Host $destination
Write-Host ""