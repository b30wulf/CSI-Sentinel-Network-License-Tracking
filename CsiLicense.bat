@echo off
:flag
start "lsmonList" cmd /k "\\gs-5\Computers and Structures\Sentinel RMS 9.7 Utilities\NetKey2\lsmon.exe" gs-5 ^> test.txt 2^>^&1
timeout /t 30
:loop
timeout /t 5
>nul find "Press Enter to continue" test.txt && (
  echo Task Completed.
) || (
  goto loop
)
python3 parse.py
python3 writetohtm.py
taskkill /FI "WindowTitle eq lsmonList*" /T /F
goto flag