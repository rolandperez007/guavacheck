Clear-Host

Write-Host ""
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "     GUAVACHECK SMART PROJECT AUDIT"
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""

$AuditFolder = ".\architecture\audit"

if (!(Test-Path $AuditFolder)) {
    New-Item -ItemType Directory -Path $AuditFolder | Out-Null
}

$Excluded = @(
    "node_modules",
    ".next",
    ".git",
    ".vercel",
    "dist",
    "build",
    "coverage"
)

function Get-ProjectItems {
    param(
        [string]$Filter = "*",
        [switch]$Directory
    )

    if ($Directory) {
        Get-ChildItem -Path . -Directory -Recurse |
        Where-Object {
            $parts = $_.FullName.Split('\')
            -not ($parts | Where-Object { $_ -in $Excluded })
        }
    }
    else {
        Get-ChildItem -Path . -Filter $Filter -File -Recurse |
        Where-Object {
            $parts = $_.FullName.Split('\')
            -not ($parts | Where-Object { $_ -in $Excluded })
        }
    }
}

Write-Host "Generating filtered reports..." -ForegroundColor Yellow

Get-ProjectItems package.json |
Select FullName |
Out-File "$AuditFolder\package-files.txt"

Get-ProjectItems "tsconfig*.json" |
Select FullName |
Out-File "$AuditFolder\typescript-files.txt"

Get-ProjectItems -Directory |
Where Name -eq "app" |
Select FullName |
Out-File "$AuditFolder\app-folders.txt"

Get-ProjectItems -Directory |
Where Name -eq "components" |
Select FullName |
Out-File "$AuditFolder\components-folders.txt"

Get-ProjectItems -Directory |
Where Name -eq "public" |
Select FullName |
Out-File "$AuditFolder\public-folders.txt"

Get-ProjectItems |
Where Name -in @("next.config.js","next.config.ts","next.config.mjs") |
Select FullName |
Out-File "$AuditFolder\next-config-files.txt"

Write-Host ""
Write-Host "Smart audit completed." -ForegroundColor Green