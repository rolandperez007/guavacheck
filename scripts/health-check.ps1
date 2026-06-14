Write-Host '=== GUAVACHECK SYSTEM HEALTH ==='

Write-Host ''
Write-Host 'NODE VERSION:'
node -v

Write-Host ''
Write-Host 'NPM VERSION:'
npm -v

Write-Host ''
Write-Host 'NEXT BUILD TEST:'
npm run build

Write-Host ''
Write-Host 'GIT STATUS:'
git status

Write-Host ''
Write-Host '=== SYSTEM COMPLETE ==='
