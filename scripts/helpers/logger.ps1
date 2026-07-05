<#
===============================================================================
GUAVA PLATFORM GENERATOR
LOGGER MODULE

Provides standardized console output for all Guava generator scripts.

Version : 2.0
===============================================================================
#>

# -------------------------------------------------------------------------
# Colors
# -------------------------------------------------------------------------

$Global:ColorInfo    = "Cyan"
$Global:ColorSuccess = "Green"
$Global:ColorWarning = "Yellow"
$Global:ColorError   = "Red"
$Global:ColorTitle   = "White"
$Global:ColorBorder  = "DarkGray"

# -------------------------------------------------------------------------
# Banner
# -------------------------------------------------------------------------

function Show-Banner {

    Clear-Host

    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host "           GUAVA PLATFORM GENERATOR v2.0" -ForegroundColor Green
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host " Engineering Intelligence Platform Scaffolding SDK"
    Write-Host ""
}

# -------------------------------------------------------------------------
# Section
# -------------------------------------------------------------------------

function Write-Section {

    param(
        [Parameter(Mandatory)]
        [string]$Title
    )

    Write-Host ""
    Write-Host "------------------------------------------------------------" -ForegroundColor $Global:ColorBorder
    Write-Host (" {0}" -f $Title) -ForegroundColor $Global:ColorTitle
    Write-Host "------------------------------------------------------------" -ForegroundColor $Global:ColorBorder
}

# -------------------------------------------------------------------------
# Messages
# -------------------------------------------------------------------------

function Write-Info {

    param(
        [Parameter(Mandatory)]
        [string]$Message
    )

    Write-Host "[INFO ] $Message" -ForegroundColor $Global:ColorInfo
}

function Write-Good {

    param(
        [Parameter(Mandatory)]
        [string]$Message
    )

    Write-Host "[ OK  ] $Message" -ForegroundColor $Global:ColorSuccess
}

function Write-Skip {

    param(
        [Parameter(Mandatory)]
        [string]$Message
    )

    Write-Host "[SKIP ] $Message" -ForegroundColor $Global:ColorWarning
}

function Write-WarningMessage {

    param(
        [Parameter(Mandatory)]
        [string]$Message
    )

    Write-Host "[WARN ] $Message" -ForegroundColor $Global:ColorWarning
}

function Write-ErrorMessage {

    param(
        [Parameter(Mandatory)]
        [string]$Message
    )

    Write-Host "[FAIL ] $Message" -ForegroundColor $Global:ColorError
}

# -------------------------------------------------------------------------
# Success Block
# -------------------------------------------------------------------------

function Write-SuccessBlock {

    param(
        [Parameter(Mandatory)]
        [string]$Message
    )

    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host (" SUCCESS : {0}" -f $Message) -ForegroundColor Green
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host ""
}

# -------------------------------------------------------------------------
# Error Block
# -------------------------------------------------------------------------

function Write-ErrorBlock {

    param(
        [Parameter(Mandatory)]
        [string]$Message
    )

    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host (" ERROR : {0}" -f $Message) -ForegroundColor Red
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host ""
}

# -------------------------------------------------------------------------
# Summary
# -------------------------------------------------------------------------

function Write-Summary {

    param(
        [int]$FoldersCreated = 0,
        [int]$FoldersSkipped = 0,
        [int]$FilesCreated = 0,
        [int]$FilesSkipped = 0
    )

    Write-Section "Generation Summary"

    Write-Host ""

    Write-Good ("Folders Created : {0}" -f $FoldersCreated)
    Write-Skip ("Folders Skipped : {0}" -f $FoldersSkipped)

    Write-Good ("Files Created   : {0}" -f $FilesCreated)
    Write-Skip ("Files Skipped   : {0}" -f $FilesSkipped)

    Write-Host ""
}

# -------------------------------------------------------------------------
# Footer
# -------------------------------------------------------------------------

function Show-Footer {

    Write-Host ""
    Write-Host "Generation Complete." -ForegroundColor Green
    Write-Host ""
}

