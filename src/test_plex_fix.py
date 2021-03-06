import unittest

class Test_convert_titleSort(unittest.TestCase):

    def test_noChange(self):
        from plex_fix import convert_titleSort
        result = convert_titleSort('No change as there only ASCII characters')
        self.assertEqual(result, 'No change as there only ASCII characters')

    def test_simple(self):
        from plex_fix import convert_titleSort
        result = convert_titleSort('Basic Абв')
        self.assertEqual(result, 'Basic Абв ## абв')

    def test_duplicates_ignored(self):
        from plex_fix import convert_titleSort
        result = convert_titleSort('Абв абв')
        self.assertEqual(result, 'Абв абв')

    def test_revert(self):
        from plex_fix import convert_titleSort
        result = convert_titleSort('Basic Абв ## basic абв', True)
        self.assertEqual(result, 'Basic Абв')

    def test_convert_russian(self):
        from plex_fix import convert_titleSort
        result = convert_titleSort('АБВГДЕЁЖЗИЙК ЛМНОПРСТУФ ХЦЧШЩЪЫЬЭЮЯ')
        self.assertEqual(result, 'АБВГДЕЁЖЗИЙК ЛМНОПРСТУФ ХЦЧШЩЪЫЬЭЮЯ ## абвгдеёжзийк лмнопрстуф хцчшщъыьэюя')

    def test_convert_ukrainian(self):
        from plex_fix import convert_titleSort
        result = convert_titleSort('АаБбВвГгҐґДдЕе ЄєЖжЗзИиІіЇїЙй КкЛлМмНнОоПпРр СсТтУуФфХхЦцЧч ШшЩщЬьЮюЯя')
        self.assertEqual(result, 'АаБбВвГгҐґДдЕе ЄєЖжЗзИиІіЇїЙй КкЛлМмНнОоПпРр СсТтУуФфХхЦцЧч ШшЩщЬьЮюЯя ## ааббввггґґддее єєжжззииііїїйй ккллммннооппрр ссттууффххццчч шшщщььююяя')

    def test_convert_greek(self):
        from plex_fix import convert_titleSort
        result = convert_titleSort('ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ')
        self.assertEqual(result, 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ ## αβγδεζηθικλμνξοπρστυφχψω')

    def test_convert_additional_characters(self):
        from plex_fix import convert_titleSort
        result = convert_titleSort('ĐÂĂÊÔƠƯẤẮẾỐỚỨẦẰỀỒỜỪẬẶỆỘỢỰ')
        self.assertEqual(result, 'ĐÂĂÊÔƠƯẤẮẾỐỚỨẦẰỀỒỜỪẬẶỆỘỢỰ ## đâăêôơưấắếốớứầằềồờừậặệộợự')

class Test_parse_and_validate_args(unittest.TestCase):

    def test_error_no_authentication(self):
        from plex_fix import parse_and_validate_args
        
        with self.assertRaises(SystemExit):
            parse_and_validate_args(['srv1'])

    def test_error_no_password(self):
        from plex_fix import parse_and_validate_args

        with self.assertRaises(SystemExit):
            parse_and_validate_args(['--user', 'u2', 'srv1'])

    def test_token(self):
        from plex_fix import parse_and_validate_args

        args = parse_and_validate_args(['--token', 'abc_token', 'srv1'])

        self.assertEqual (args.token, 'abc_token')
        self.assertEqual (args.server_name, 'srv1')

    def test_userPass(self):
        from plex_fix import parse_and_validate_args

        args = parse_and_validate_args(['--user', 'u2', '--password', 'p2', 'srv2'])

        self.assertEqual(args.user, 'u2')
        self.assertEqual(args.password, 'p2')
        self.assertEqual (args.server_name, 'srv2')

    def test_libraryName(self):
        from plex_fix import parse_and_validate_args

        args = parse_and_validate_args(['--token', 'abc_token', 'srv1', '--library', 'libraryname'])

        self.assertEqual (args.token, 'abc_token')
        self.assertEqual (args.server_name, 'srv1')
        self.assertEqual (args.library, 'libraryname')

    def test_preview(self):
        from plex_fix import parse_and_validate_args

        args = parse_and_validate_args(['--token', 'abc_token', '--preview', 'srv1'])

        self.assertEqual (args.token, 'abc_token')
        self.assertEqual (args.server_name, 'srv1')
        self.assertEqual (args.preview, True)

if __name__ == '__main__':
    unittest.main()