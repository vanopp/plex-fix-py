@set /p username="Enter plex email or username: "
@set /p password="Enter password: "
@echo.
python %~dp0src/plex_fix.py -u %username% -p %password% -l nonexistinglibrary %COMPUTERNAME%