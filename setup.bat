@echo off

echo Installing bakasable

md "C:\Program Files\bakasable"

md "C:\Program Files\bakasable\cache"

copy .\bin\windows\bakasable.exe "C:\Program Files\bakasable\"

setx /M path "%path%;C:\Program Files\bakasable\"

