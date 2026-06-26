Clear-Host

$Report = ".\architecture\migration\reports"

if (!(Test-Path $Report)) {
    New-Item -ItemType Directory -Path $Report | Out-Null
}

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "      GUAVACHECK MODULE INVENTORY"
Write-Host "========================================="
Write-Host ""

$Folders = @(
    "app",
    "components",
    "hooks",
    "contexts",
    "services",
    "lib",
    "pages",
    "utils",
    "types",
    "store",
    "data",
    "public"
)

foreach($Folder in $Folders){

    if(Test-Path $Folder){

        Write-Host "Scanning $Folder..."

        Get-ChildItem $Folder -Recurse -File |
        Select-Object FullName |
        Out-File "$Report\$($Folder)-files.txt"

    }

}

Write-Host ""
Write-Host "Inventory completed." -ForegroundColor Green