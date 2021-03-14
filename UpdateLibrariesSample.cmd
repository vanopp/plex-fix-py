@rem Please note DOS encoding
python %~dp0src\plex_fix.py -t %PlexToken% -l Фильмы %COMPUTERNAME%
python %~dp0src\plex_fix.py -t %PlexToken% -l Сериалы %COMPUTERNAME%