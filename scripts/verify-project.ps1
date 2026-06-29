$critical = @(
"package.json",
"tsconfig.json",
"next.config.js",
"README.md",
"ROADMAP.md"
)

Write-Host ""

foreach($file in $critical){

if(Test-Path $file){

Write-Host "[OK] $file"

}

else{

Write-Host "[MISSING] $file"

}

}

Write-Host ""