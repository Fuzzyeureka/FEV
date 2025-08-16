@echo off

:main
echo 1.add mods/rp/sp
echo 2.remove mods/rp/sp
echo 3.refresh index
echo 4.export
set /p input="what do you want to do > "

if /I %input% equ 1 goto add
if /I %input% equ 2 goto remove
if /I %input% equ 3 call packwiz refresh
if /I %input% equ 4 call packwiz modrinth export
pause
cls
goto main

:add
set /p add="what do you want to add > "
packwiz modrinth add %add%
pause
cls
goto main

:remove
set /p remove="what do you want to remove > "
packwiz remove %remove%
pause
cls
goto main