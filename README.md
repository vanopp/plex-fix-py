# Fix non-ASCII Plex search

Many years [Plex media server](https://www.plex.tv/) have an annoying issue where non-ASCII characters such as cyrillic or greek searched in a case-sensitive manner which leads to the unusable search.
The issue raised multiple times on the [Reddit](https://www.reddit.com/r/PleX/comments/f7czff/search_should_be_case_and_diacritics_insensitive/) and [Official Plex forum](https://forums.plex.tv/t/search-is-case-sensitive-with-cyrillic-characters/141491)

Here the python script which fixes the issue by modifying the 'Sort Title' property of all of the Plex catalog items subject to issue. Examples 'Matrix' will be unmodified and 'Матрица' will be converted to 'Матрица ## матрица'
This way Plex behavior not changed in any way except now it can search by lowercase non-ASCII characters.
All of the modifications done by this script can be reverted. Only exception sort titles already containing ' ##'

## Prequesties:
Script designed for windows but should work on other platforms too
- Python 3.7.3 or newer. [download](https://www.python.org/downloads/windows/) Hint: it is recommended to check "Add Python to path" if this is the first Python install on the machine.
- Python plexapi. Run command from the command line to obtain it: `pip install plexapi`.

## Usage samples:
Applies all the modifications with authentication by plex user name and password. Additionally prints out received reusable security token.
<pre>python plex_fix.py <b>-u "my_email@gmail.com" -p "my_password"</b> servername</pre>

Authentication with token seems to be more secure. <!--  [this arcticle](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/) explains how to get it -->
<pre>python plex_fix.py <b>-t securityToken</b> servername</pre>

Apply changes to specific library 
<pre>python plex_fix.py -t securityToken <b>--library LibraryName</b> servername</pre>

Revert changes previously done by this script to the Plex catalog:
<pre>python plex_fix.py -t securityToken <b>--revert</b> servername</pre>

Preview changes to the Plex catalog. I. e. do not modify anything, only print out modifications to be done:
<pre>python plex_fix.py -t securityToken <b>--preview</b> servername</pre>

## Development notes.
For opening sln solution file and running tests, Visual Studio 2019 Community edition or better with Python development workload installed is required. However python scripts can be edited and executed individually without Visual Studio.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
[plexapi](https://github.com/pkkid/python-plexapi) 