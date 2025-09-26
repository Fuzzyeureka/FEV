@echo off

:main
echo 1.refresh index
echo 2.export
set /p input="what do you want to do > "

if /I %input% equ 1 call packwiz refresh
if /I %input% equ 2 call packwiz modrinth export
pause
cls
goto main