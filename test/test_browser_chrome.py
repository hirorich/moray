import unittest
from unittest.mock import patch, MagicMock

from moray._browser import chrome
from moray.exception import SupportError

class ChromeTest(unittest.TestCase):
    
    def test_create_command_1(self):
        path = 'chrome.exe'
        url = 'http://localhost:port/'
        cmdline_args = []
        
        correct = [path, '--app={0}'.format(url)]
        
        self.assertEqual(chrome.create_command(path, url, cmdline_args), correct)
    
    def test_create_command_2(self):
        path = 'path'
        url = 'url'
        cmdline_args = ['--disable-http-cache', '--incognito']
        
        correct = [path, '--app={0}'.format(url), '--disable-http-cache', '--incognito']
        
        self.assertEqual(chrome.create_command(path, url, cmdline_args), correct)
    
    def test_find_chrome_windows_1(self):
        
        mock_value = [
            ([MagicMock(), MagicMock()], [('chrome1', None), ('chrome2', None)], [True, False], 'chrome1'),
            ([MagicMock(), MagicMock()], [('chrome1', None), ('chrome2', None)], [False, True], 'chrome2'),
            ([MagicMock(), MagicMock()], [('chrome1', None), ('chrome2', None)], [True, True], 'chrome1')
        ]
        
        for key, value, file, correct in mock_value:
            with (patch('winreg.OpenKey', side_effect = key) as ok,
                patch('winreg.QueryValueEx', side_effect = value) as ove,
                patch('os.path.isfile', side_effect = file) as opi
            ):
                try:
                    self.assertEqual(chrome._find_chrome_windows(), correct)
                except Exception as e:
                    self.fail()
    
    def test_find_chrome_windows_2(self):
        error_msg = '"chrome.exe" is not found.'
        
        mock_value = [
            ([OSError('OpenKey'), OSError('OpenKey')], [None, None], [True, True]),
            ([MagicMock(), MagicMock()], [OSError('QueryValueEx'), OSError('QueryValueEx')], [True, True]),
            ([MagicMock(), MagicMock()], [(None, None), (None, None)], [False, False])
        ]
        
        for key, value, file in mock_value:
            with (patch('winreg.OpenKey', side_effect = key) as ok,
                patch('winreg.QueryValueEx', side_effect = value) as ove,
                patch('os.path.isfile', side_effect = file) as opi
            ):
                try:
                    chrome._find_chrome_windows()
                    self.fail()
                except Exception as e:
                    self.assertIs(type(e), FileNotFoundError)
                    self.assertEqual(e.args[0], error_msg)
    
    @patch('moray._browser.chrome._find_chrome_windows', return_value = "chrome.exe")
    def test_find_path_1(self, mock_obj):
        for platform in 'win32', 'win64':
            with patch('sys.platform', platform) as sys_platform:
                try:
                    self.assertEqual(chrome.find_path(), "chrome.exe")
                except Exception as e:
                    self.fail()
    
    @patch('sys.platform', 'IE')
    def test_find_path_2(self):
        error_msg = 'This OS is not a supported OS.'
        
        try:
            chrome.find_path()
            self.fail()
        except Exception as e:
            self.assertIs(type(e), SupportError)
            self.assertEqual(e.args[0], error_msg)
