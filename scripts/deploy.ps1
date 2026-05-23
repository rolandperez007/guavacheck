Write-Host '=== CLEAN DEPLOY START ==='

Remove-Item -Recurse -Force .next -ErrorAction SilentlyContinue

git add .

git commit -m 'Production sync update'

git push

Write-Host '=== DEPLOY COMPLETE ==='
