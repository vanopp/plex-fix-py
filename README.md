# Fix non-ASCII Plex search

Many years [Plex media server](https://www.plex.tv/) have an annoying issue where non-ASCII characters such as cyrillic or greek searched in a case-sensitive manner which leads to the unusable search for a large part of the community.
Issue discussed on [Reddit](https://www.reddit.com/r/PleX/comments/f7czff/search_should_be_case_and_diacritics_insensitive/) and on [Official Plex forum](https://forums.plex.tv/t/search-is-case-sensitive-with-cyrillic-characters/141491)

Here the python script which fixes the issue by modifying the 'Sort Title' property of all of the Plex catalog items subject to issue. Examples 'Matrix' will be unmodified and 'Матрица' will be converted to 'Матрица ## матрица'
This way Plex behavior not changed in any way except one detail: now it can search by lowercase non-ASCII characters.
All of the modifications done by this script can be reverted. Only exception sort titles already containing ' ##'

## Prequesties:
Script designed for windows but should work on other platforms too
- Python 3.7.3 or newer. [download](https://www.python.org/downloads/windows/)
- Python plexapi. Run command from the command line to obtain it: `pip install plexapi`.

## Usage samples:
Applies all the modifications with authorization by plex user name and password
<pre>python plex_fix.py <b>-u "my_email@gmail.com" -p "my_password"</b> servername</pre>

Applies all the modifications with authorization by plex token
<pre>python plex_fix.py <b>-t tokenTokenTokenToken</b> servername</pre>
authorization token seems to be more secure, [this arcticle](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/) explains how to get it. Also authorization by username and password with script print received token to console.

Apply changes to specific library 
<pre>python plex_fix.py -t tokenTokenTokenToken <b>--library LibraryName</b> servername</pre>

Revert changes previously done by this script to the Plex catalog:
<pre>python plex_fix.py -t tokenTokenTokenToken <b>--revert</b> servername</pre>

Preview changes to the Plex catalog:
<pre>python plex_fix.py -t tokenTokenTokenToken <b>--preview</b> servername</pre>
I. e. script will not modify anything, only prints out modifications to be done.

## Development notes.
For opening sln solution file and running tests, Visual Studio 2019 Community edition or better with Python development workload installed is required. However main script plex-fix.py can be edited and executed individually without Visual Studio.

## License
plexapi [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)