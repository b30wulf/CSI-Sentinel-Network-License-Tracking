@echo off
call getCmdPID
set "current_pid=%errorlevel%"
start cmd.exe /c "cd /d "G:\license parsing bot""
start cmd.exe /c ""\\gs-5\Computers and Structures\Sentinel RMS 9.7 Utilities\NetKey2\lsmon.exe" gs-5 > test.txt 2>&1"
timeout /t 15
for /f "skip=3 tokens=2 delims= " %%a in ('tasklist /fi "imagename eq cmd.exe"') do (
    if "%%a" neq "%current_pid%" (
        TASKKILL /PID %%a /f >nul 2>nul
    )
)
python3 parse.py
python3 writetohtm.py
start license.html