$myPid = $PID
$procs = Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -and $_.CommandLine -match 'uvicorn' -and $_.ProcessId -ne $myPid }
if ($procs) {
  foreach ($p in $procs) {
    Write-Output "Killing PID:$($p.ProcessId) CMD:$($p.CommandLine)"
    try {
      Stop-Process -Id $p.ProcessId -Force -ErrorAction Stop
      Write-Output "KILLED:$($p.ProcessId)"
    } catch {
      Write-Output "FAILED:$($p.ProcessId) $_"
    }
  }
} else {
  Write-Output "No uvicorn processes found"
}
