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
        correct = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        
        self.assertEqual(chrome._find_chrome_windows(), correct)
    
    def test_find_chrome_windows_2(self):
        error_msg = '"chrome.exe" is not found.'
        
        with patch('winreg.OpenKey', return_value = None) as m:
            try:
                chrome._find_chrome_windows()
            except Exception as e:
                self.assertIs(type(e), FileNotFoundError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_find_chrome_windows_3(self):
        error_msg = '"chrome.exe" is not found.'
        
        with patch('winreg.QueryValue', return_value = None) as m:
            try:
                chrome._find_chrome_windows()
            except Exception as e:
                self.assertIs(type(e), FileNotFoundError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_find_chrome_windows_4(self):
        error_msg = '"chrome.exe" is not found.'
        
        with patch('os.path.isfile', return_value = False) as m:
            try:
                chrome._find_chrome_windows()
            except Exception as e:
                self.assertIs(type(e), FileNotFoundError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_find_path_1(self):
        correct = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        
        self.assertEqual(chrome.find_path(), correct)
    
    def test_find_path_2(self):
        error_msg = 'This OS is not a supported OS.'
        
        with patch('sys.platform', return_value = 'IE') as m:
            try:
                chrome.find_path()
            except Exception as e:
                self.assertIs(type(e), SupportError)
                self.assertEqual(e.args[0], error_msg)
