@echo off
python "Update version.py"

set /p version="enter version you'd like to update > "

if not exist "versions/%version%" (
    echo stairwell 87 does not exist.
    pause
)

pushd "versions/%version%"
call "update mods.bat"