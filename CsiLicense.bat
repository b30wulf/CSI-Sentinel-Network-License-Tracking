@echo off
echo Press Enter...
"\\gs-5\Computers and Structures\Sentinel RMS 9.7 Utilities\NetKey2\lsmon.exe" gs-5 > test.txt 2>&1
python3 parse.py
python3 writetohtm.py
start license.html