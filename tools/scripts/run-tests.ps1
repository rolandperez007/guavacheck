$config = Get-Content "C:\Dev\projects\guavacheck\system-test.json" -Raw | ConvertFrom-Json

Write-Host ""
Write-Host "==========================="
Write-Host "GUAVACHECK SYSTEM TEST"
Write-Host "==========================="
Write-Host ""

Write-Host "Project:" $config.project.name
Write-Host "Framework:" $config.project.framework
Write-Host "Backend:" $config.project.backend
Write-Host ""

Write-Host "TEST STATUS"
Write-Host "----------------"

$config.tests.PSObject.Properties | ForEach-Object {

    if ($_.Value -eq $true) {
        Write-Host "[PASS]" $_.Name
    }
    else {
        Write-Host "[FAIL]" $_.Name
    }

}

Write-Host ""
Write-Host "AVAILABLE ROUTES"
Write-Host "----------------"

foreach ($route in $config.routes) {
    Write-Host $route.name ":" $route.path
}

Write-Host ""
Write-Host "Local URL:" $config.deployment.local_url
Write-Host "Production:" $config.deployment.production_domain

Write-Host ""
Write-Host "GUAVACHECK TEST COMPLETE"