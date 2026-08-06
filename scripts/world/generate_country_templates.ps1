# ============================================
# GUAVA WORLD ENGINE
# Country Template Generator
# ============================================

$templateFiles = @(
"README.md",
"01-identity.md",
"02-government.md",
"03-geography.md",
"04-demographics.md",
"05-economy.md",
"06-currency.md",
"07-banking.md",
"08-taxation.md",
"09-mortgages.md",
"10-property.md",
"11-construction.md",
"12-legal.md",
"13-localization.md",
"14-utilities.md",
"15-transport.md",
"16-security.md",
"17-austin.md"
)

$continents = @(
"africa",
"asia",
"europe",
"middle-east",
"north-america",
"south-america",
"oceania"
)

$root = ".\docs\world\countries"

$totalCountries = 0
$totalFiles = 0

foreach ($continent in $continents)
{
    $continentPath = Join-Path $root $continent

    if (!(Test-Path $continentPath))
    {
        continue
    }

    $countries = Get-ChildItem $continentPath -Directory

    foreach ($country in $countries)
    {
        $totalCountries++

        foreach ($file in $templateFiles)
        {
            $path = Join-Path $country.FullName $file

            if (!(Test-Path $path))
            {
                New-Item -ItemType File -Force $path | Out-Null
                $totalFiles++
            }
        }
    }
}

Write-Host ""
Write-Host "===================================="
Write-Host " WORLD ENGINE TEMPLATE COMPLETE"
Write-Host "===================================="
Write-Host ""
Write-Host "Countries :" $totalCountries
Write-Host "Files Created :" $totalFiles
Write-Host ""