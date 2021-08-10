import unittest

from moray._browser import chrome

class ChromeTest(unittest.TestCase):
    
    def test_create_command(self):
        path = 'chrome.exe'
        url = 'http://localhost:port/'
        cmdline_args = []
        
        corect = [path, '--app={0}'.format(url)]
        
        self.assertEqual(chrome.create_command(path, url, cmdline_args), corect)
    
    def test_create_command2(self):
        path = 'path'
        url = 'url'
        cmdline_args = ['--disable-http-cache', '--incognito']
        
        corect = [path, '--app={0}'.format(url), '--disable-http-cache', '--incognito']
        
        self.assertEqual(chrome.create_command(path, url, cmdline_args), corect)

