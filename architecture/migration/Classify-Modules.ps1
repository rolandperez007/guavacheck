Clear-Host

$Report = ".\architecture\migration\reports"

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "      GUAVACHECK FEATURE CLASSIFIER"
Write-Host "============================================"
Write-Host ""

$Patterns = @(
    "austin",
    "auth",
    "supabase",
    "property",
    "design",
    "floor",
    "viewer",
    "estimate",
    "cost",
    "investor",
    "dashboard",
    "report",
    "admin",
    "payment",
    "map",
    "listing",
    "search",
    "mortgage",
    "chat",
    "ai"
)

foreach ($Pattern in $Patterns) {

    Write-Host "Searching: $Pattern"

    Get-ChildItem . -Recurse -File |
    Where-Object {
        $_.FullName -notmatch "node_modules|\.next|\.git|\.vercel"
    } |
    Where-Object {
        $_.FullName.ToLower().Contains($Pattern)
    } |
    Select-Object FullName |
    Out-File "$Report\$Pattern.txt"

}