@echo off
call :Resume
goto %current%
goto :eof

:one
::Add script to Run key
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v %~n0 /d %~dpnx0 /f
echo two >%~dp0current.txt
echo Press any key to reboot the system and continue the installation 
pause
shutdown -r -t 0
goto :eof

:two
::Remove script from Run key
reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v %~n0 /f
python %~dp0main.py
pause
goto :eof

:resume
if exist %~dp0current.txt (
    set /p current=<%~dp0current.txt
) else (
    set current=one
)