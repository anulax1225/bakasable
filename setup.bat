@echo off

cd %~dp0

echo Installing bakasable

md "C:\Program Files\bakasable"

md "C:\Program Files\bakasable\cache"

xcopy /y .\bin\windows\bakasable.exe "C:\Program Files\bakasable"
xcopy /y .\bin\windows\premake5.exe "C:\Program Files\bakasable"

powershell .\path.ps1

pause