@echo off
:flag
Rem run lsmon.exe on a separate command prompt
start "lsmonList" cmd /k "\\gs-5\Computers and Structures\Sentinel RMS 9.7 Utilities\NetKey2\lsmon.exe" gs-5 ^> test.txt 2^>^&1
timeout /t 30
Rem this loop adds more time if lsmon.exe didn't finish
:loop
timeout /t 5
Rem This finds the completion of lsmon.exe by finding "Press enter to continue"
>nul find "Press Enter to continue" test.txt && (
  echo Task Completed.
) || (
  goto loop
)
python3 parse.py
python3 writetohtm.py
Rem We have to kill lsmon.exe to free test.txt to be able to write to it again.
taskkill /FI "WindowTitle eq lsmonList*" /T /F
goto flag