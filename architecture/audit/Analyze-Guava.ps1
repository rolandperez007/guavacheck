Clear-Host

$Audit = ".\architecture\audit"

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "      GUAVACHECK ARCHITECTURE"
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

function CountLines($file){
    if(Test-Path $file){
        return (Get-Content $file).Count
    }
    return 0
}

$packages   = CountLines "$Audit\package-files.txt"
$apps       = CountLines "$Audit\app-folders.txt"
$components = CountLines "$Audit\components-folders.txt"
$publics    = CountLines "$Audit\public-folders.txt"
$nodes      = CountLines "$Audit\node-modules.txt"
$configs    = CountLines "$Audit\next-config-files.txt"

Write-Host "Next.js Projects"
Write-Host "----------------"
Write-Host "package.json files : $packages"
Write-Host "app folders        : $apps"
Write-Host "components folders : $components"
Write-Host "public folders     : $publics"
Write-Host "node_modules       : $nodes"
Write-Host "Next configs       : $configs"

Write-Host ""
Write-Host "Large Files"
Write-Host "-----------"

Get-Content "$Audit\large-files.txt"

Write-Host ""
Write-Host "Git Status"
Write-Host "----------"

Get-Content "$Audit\git-status.txt"

Write-Host ""
Write-Host "Analysis Complete." -ForegroundColor Green