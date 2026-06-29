Write-Host ""
Write-Host "=========================="
Write-Host "GUAVACHECK HEALTH REPORT"
Write-Host "=========================="

Write-Host ""

Write-Host "Checking TypeScript..."

npx tsc --noEmit

Write-Host ""

Write-Host "Checking npm packages..."

npm outdated

Write-Host ""

Write-Host "Checking vulnerabilities..."

npm audit

Write-Host ""

Write-Host "Done."