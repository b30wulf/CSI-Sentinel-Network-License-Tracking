@echo off
start "lsmonList" cmd /k "\\gs-5\Computers and Structures\Sentinel RMS 9.7 Utilities\NetKey2\lsmon.exe" gs-5 ^> test.txt 2^>^&1
timeout /t 30
:loop
timeout /t 5
>nul find "Press Enter to continue" test.txt && (
  echo Task Completed.
) || (
  goto loop
)
if exist temp.txt (
    rem file exists
) else (
    type nul >temp.txt
)
if exist output.txt (
    rem file exists
) else (
    type nul >output.txt
)
if exist output1.txt(
    rem file exists
) else (
    type nul >output1.txt
)
if exist license.html (
    rem file exists
) else (
    type nul >license.html
)
python3 parse.py
python3 writetohtm.py
start license.html
taskkill /FI "WindowTitle eq lsmonList*" /T /F