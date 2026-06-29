$config = Get-Content "C:\Dev\projects\guavacheck\layout.json" -Raw | ConvertFrom-Json

$layout = @"
export const metadata = {
  title: "$($config.title)",
  description: "$($config.description)",
}

export default function RootLayout({ children }) {
  return (
    <html lang="$($config.lang)">
      <body>
        {children}
      </body>
    </html>
  )
}
"@

Set-Content -Path "C:\Dev\projects\guavacheck\app\layout.jsx" -Value $layout

Write-Host "Layout generated successfully from JSON"