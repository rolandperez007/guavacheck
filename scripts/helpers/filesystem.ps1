<#
===============================================================================
GUAVA PLATFORM GENERATOR
Filesystem Helper

Version : 2.0

Purpose
-------
Provides safe filesystem operations used by the generator.

===============================================================================
#>

Set-StrictMode -Version Latest
$script:PathSeparator = [System.IO.Path]::DirectorySeparatorChar

# ------------------------------------------------------------
# Normalize Path
# ------------------------------------------------------------

function Normalize-Path {

    param(
        [Parameter(Mandatory)]
        [string]$Path
    )

    return $Path.Replace("/", [System.IO.Path]::DirectorySeparatorChar)
}

# ------------------------------------------------------------
# Test Folder
# ------------------------------------------------------------

function Folder-Exists {

    param(
        [Parameter(Mandatory)]
        [string]$Path
    )

    return Test-Path (Normalize-Path $Path)
}

# ------------------------------------------------------------
# Ensure Folder
# ------------------------------------------------------------

function Ensure-Folder {

    param(
        [Parameter(Mandatory)]
        [string]$Path
    )

    $Path = Normalize-Path $Path

    if ([string]::IsNullOrWhiteSpace($Path)) {
        return
    }

    if (!(Test-Path $Path)) {

        New-Item `
            -ItemType Directory `
            -Path $Path `
            -Force | Out-Null

        Write-Good "Created Folder : $Path"

    }
    else {

        Write-Skip "Folder Exists : $Path"

    }

}

# ------------------------------------------------------------
# Ensure Parent Folder
# ------------------------------------------------------------

function Ensure-ParentFolder {

    param(
        [Parameter(Mandatory)]
        [string]$FilePath
    )

    $parent = Split-Path $FilePath

    Ensure-Folder $parent

}

# ------------------------------------------------------------
# File Exists
# ------------------------------------------------------------

function File-Exists {

    param(
        [Parameter(Mandatory)]
        [string]$Path
    )

    return Test-Path (Normalize-Path $Path)

}

# ------------------------------------------------------------
# Create Empty File
# ------------------------------------------------------------

function New-EmptyFile {

    param(
        [Parameter(Mandatory)]
        [string]$Path,

        [switch]$Force
    )

    $Path = Normalize-Path $Path

    Ensure-ParentFolder $Path

    if ((Test-Path $Path) -and !$Force) {

        Write-Skip "File Exists : $Path"

        return $false

    }

    Set-Content `
        -Path $Path `
        -Value "" `
        -Encoding UTF8

    Write-Good "Created File : $Path"

    return $true

}

# ------------------------------------------------------------
# Write File
# ------------------------------------------------------------

function Write-File {

    param(

        [Parameter(Mandatory)]
        [string]$Path,

        [Parameter(Mandatory)]
        [string]$Content,

        [switch]$Force

    )

    $Path = Normalize-Path $Path

    Ensure-ParentFolder $Path

    if ((Test-Path $Path) -and !$Force) {

        Write-Skip "Skipped File : $Path"

        return $false

    }

    Set-Content `
        -Path $Path `
        -Value $Content `
        -Encoding UTF8

    Write-Good "Written File : $Path"

    return $true

}

# ------------------------------------------------------------
# Append File
# ------------------------------------------------------------

function Append-File {

    param(

        [Parameter(Mandatory)]
        [string]$Path,

        [Parameter(Mandatory)]
        [string]$Content

    )

    Ensure-ParentFolder $Path

    Add-Content `
        -Path $Path `
        -Value $Content `
        -Encoding UTF8

    Write-Good "Updated File : $Path"

}
# ------------------------------------------------------------
# Delete File
# ------------------------------------------------------------

function Remove-SafeFile {

    param(

        [Parameter(Mandatory)]
        [string]$Path

    )

    $Path = Normalize-Path $Path

    if (!(Test-Path $Path)) {

        Write-Skip "File Missing : $Path"

        return

    }

    Remove-Item `
        -Path $Path `
        -Force

    Write-Good "Deleted File : $Path"

}

# ------------------------------------------------------------
# Delete Folder
# ------------------------------------------------------------

function Remove-SafeFolder {

    param(

        [Parameter(Mandatory)]
        [string]$Path

    )

    $Path = Normalize-Path $Path

    if (!(Test-Path $Path)) {

        Write-Skip "Folder Missing : $Path"

        return

    }

    Remove-Item `
        -Path $Path `
        -Recurse `
        -Force

    Write-Good "Deleted Folder : $Path"

}

# ------------------------------------------------------------
# Read File
# ------------------------------------------------------------

function Read-File {

    param(

        [Parameter(Mandatory)]
        [string]$Path

    )

    $Path = Normalize-Path $Path

    if (!(Test-Path $Path)) {

        throw "File not found: $Path"

    }

    return Get-Content `
        -Path $Path `
        -Raw

}

# ------------------------------------------------------------
# Copy File
# ------------------------------------------------------------

function Copy-SafeFile {

    param(

        [Parameter(Mandatory)]
        [string]$Source,

        [Parameter(Mandatory)]
        [string]$Destination,

        [switch]$Force

    )

    Ensure-ParentFolder $Destination

    if ((Test-Path $Destination) -and !$Force) {

        Write-Skip "Destination Exists : $Destination"

        return

    }

    Copy-Item `
        -Path $Source `
        -Destination $Destination `
        -Force

    Write-Good "Copied : $Destination"

}

# ------------------------------------------------------------
# Directory Tree
# ------------------------------------------------------------

function Get-RelativeTree {

    param(

        [Parameter(Mandatory)]
        [string]$Root

    )

    $Root = Normalize-Path $Root

    if (!(Test-Path $Root)) {

        return @()

    }

    return Get-ChildItem `
        -Path $Root `
        -Recurse

}

# ------------------------------------------------------------
# Timestamp
# ------------------------------------------------------------

function Get-TimeStamp {

    return Get-Date -Format "yyyy-MM-dd HH:mm:ss"

}

# ------------------------------------------------------------
# Project Verification
# ------------------------------------------------------------

function Test-GuavaProject {

    param(

        [string]$Root = (Resolve-Path .)

    )

    $required = @(
        "backend",
        "scripts"
    )

    foreach ($item in $required) {

        if (!(Test-Path (Join-Path $Root $item))) {

            Write-ErrorMessage "Missing project folder: $item"

            return $false

        }

    }

    Write-Good "Guava project verified."

    return $true

}

# ------------------------------------------------------------
# Filesystem Ready
# ------------------------------------------------------------

Write-Info "Filesystem helper loaded."