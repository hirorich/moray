import unittest
from unittest.mock import patch

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
            {'key' : [None, None], 'value' : [('chrome1', None), ('chrome2', None)], 'file' : [True, False], 'correct' : 'chrome1'},
            {'key' : [None, None], 'value' : [('chrome1', None), ('chrome2', None)], 'file' : [False, True], 'correct' : 'chrome2'},
            {'key' : [None, None], 'value' : [('chrome1', None), ('chrome2', None)], 'file' : [True, True], 'correct' : 'chrome1'}
        ]
        
        for value in mock_value:
            
            with (patch('winreg.OpenKey', side_effect = value['key']) as ok,
                patch('winreg.QueryValueEx', side_effect = value['value']) as ove,
                patch('os.path.isfile', side_effect = value['file']) as opi
            ):
                try:
                    self.assertEqual(chrome._find_chrome_windows(), value['correct'])
                except Exception as e:
                    self.fail()
    
    def test_find_chrome_windows_2(self):
        error_msg = '"chrome.exe" is not found.'
        
        mock_value = [
            {'key' : [OSError('OpenKey'), OSError('OpenKey')], 'value' : [None, None], 'file' : [True, True]},
            {'key' : [None, None], 'value' : [OSError('QueryValueEx'), OSError('QueryValueEx')], 'file' : [True, True]},
            {'key' : [None, None], 'value' : [(None, None), (None, None)], 'file' : [False, False]}
        ]
        
        for value in mock_value:
            
            with (patch('winreg.OpenKey', side_effect = value['key']) as ok,
                patch('winreg.QueryValueEx', side_effect = value['value']) as ove,
                patch('os.path.isfile', side_effect = value['file']) as opi
            ):
                try:
                    chrome._find_chrome_windows()
                    self.fail()
                except Exception as e:
                    self.assertIs(type(e), FileNotFoundError)
                    self.assertEqual(e.args[0], error_msg)
    
    def test_find_path_1(self):
        correct = "chrome.exe"
        
        for platform in 'win32', 'win64':
            with (
                patch('sys.platform', platform) as sys_platform,
                patch('moray._browser.chrome._find_chrome_windows', return_value = correct) as find_chrome_windows
            ):
                try:
                    self.assertEqual(chrome.find_path(), correct)
                except Exception as e:
                    self.fail()
    
    def test_find_path_2(self):
        error_msg = 'This OS is not a supported OS.'
        
        with patch('sys.platform', 'IE') as platform:
            try:
                chrome.find_path()
            except Exception as e:
                self.assertIs(type(e), SupportError)
                self.assertEqual(e.args[0], error_msg)
