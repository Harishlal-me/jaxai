@echo off
REM Valorant Launcher Script
REM This bypasses Windows permission issues

echo Launching Valorant...

REM Try method 1: Direct launch
start "" "E:\VALORANT\Riot Games\VALORANT\live\VALORANT.exe"

REM If that fails, try the Riot Client
if errorlevel 1 (
    echo Direct launch failed, trying Riot Client...
    start "" "E:\VALORANT\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant --launch-patchline=live
)

exit
