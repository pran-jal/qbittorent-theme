$themePath = "Night-Owl-Theme.qbtheme"
$themeSrcPath = "./src"
$requiredResources = @("resource.qrc", "config.json", "stylesheet.qss")

foreach ($resource in $requiredResources){
    if (!(Test-Path "$themeSrcPath/$resource")){
        Write-Host "Missing $resource for theme." -ForegroundColor Red
        Exit
    }
}

if (!(Test-Path "rcc.exe")) {
    Write-Host "ERROR: rcc.exe not found." -ForegroundColor Red
    Exit
}

"rcc.exe" "$themeSrcPath/resource.qrc" -o "$themePath" -binary
Write-Host "Night-Owl-Theme created Successfully."
