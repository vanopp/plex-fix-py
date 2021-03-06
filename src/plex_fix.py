from plexapi.myplex import MyPlexAccount
from plexapi.myplex import Unauthorized
from plexapi.myplex import BadRequest
from plexapi.myplex import NotFound
import argparse
import sys

SPLITTER = ' ##'

def convert_titleSort(title, revert = False):
    originalTitleSort = (title.split(SPLITTER)[0]).strip()
    if revert: 
        return originalTitleSort

    result = ''
    originalArray = originalTitleSort.split(' ')
    for str in originalArray:
        if ascii(str) != "'" + str + "'" \
        and str != str.lower() \
        and not str.lower() in originalArray:
            result = result + ' ' + str.lower()

    if result == '': return originalTitleSort

    return originalTitleSort + SPLITTER + result

def parse_and_validate_args(args1):
    parser = argparse.ArgumentParser(description='Fixes Plex search using non-ASCII characters by modifying "Sort Title"', \
)#                usage='%(prog)s y [-h] [(-u USER -p PASSWORD) | -t TOKEN] [--library library_name] [--preview] [--revert] server_name')

    parser.add_argument('-u', '--user', help="Plex user name")
    parser.add_argument('-p', '--password', help="Plex password")
    parser.add_argument('-t', '--token', help="Plex token")
    parser.add_argument('server_name', help="Plex server name")
    parser.add_argument('-l', '--library', help="Plex library name")
    parser.add_argument('-w', '--preview', action='store_true', help="Do not modify library. Allows to preview changes")
    parser.add_argument('-r', '--revert', action='store_true', help="Revert all changes applied previously")
    
    args = parser.parse_args(args1)
    if (args.user is not None and args.password is None) \
        or (args.user is None and args.password is not None):
        parser.error("Please provide both username and password")
    if (args.token is None and args.user is None) \
        or (args.token is not None and args.user is not None):
        parser.error("Please provide a token or username with a password.")
    return args

def main():
    args = parse_and_validate_args(sys.argv[1:])

    print('Log in to ' + args.server_name + 'Plex server')
    try:
        account = MyPlexAccount(username = args.user, password = args.password, token = args.token)
    except Unauthorized as err:
        sys.exit("Unable to log in: {0}".format(err))
    except BadRequest as err:
        sys.exit("Unable to log in: {0}".format(err))
    
#        raise

    if args.token is None:
        print('token is ' + account.authenticationToken)

    printPrefix = ''
    if args.preview:
        printPrefix = '[Preview] '

    print(printPrefix + 'Connecting to ' + args.server_name)
    plex = account.resource(args.server_name).connect()

    if args.library is None:
        print(printPrefix + 'Retrieving libraries contents')
        movies = plex.library.search()
    else:
        print(printPrefix + 'Retrieving library ' + args.library + ' contents')
        try:
            movies = plex.library.section(args.library).search()
        except NotFound as err:
            sys.exit(err)

    updated = 0
    ignored = 0
    for movie in movies:
        if movie.titleSort != None :
            newTitleSort = convert_titleSort(movie.titleSort, args.revert)
            if newTitleSort != movie.titleSort:
                print(printPrefix + 'Modify Sort Title "' + movie.titleSort + '" to "' + newTitleSort + '"')
                if not args.preview:
                    values = {'titleSort.value': newTitleSort, 'titleSort.locked': 1}
                    movie.edit(**values)

                updated += 1
            else:
                ignored += 1

    print(printPrefix + 'Done. Updated ' + str(updated) + ' items, ignored ' + str(ignored) + ' items.')

if __name__ == '__main__':
    main()