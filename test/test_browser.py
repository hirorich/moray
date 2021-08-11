import unittest
from unittest.mock import patch, MagicMock

from moray import _browser
from moray.exception import SupportError

class BrowserTest(unittest.TestCase):
    
    def test_is_supported_1(self):
        self.assertEqual(_browser.is_supported('chrome'), True)
    
    
    def test_is_supported_2(self):
        self.assertEqual(_browser.is_supported('edge'), False)
    
    def test_open_1(self):
        
        with(
            patch('moray._browser._browser_modules', {'chrome': MagicMock()}) as bm,
            patch('subprocess.Popen', MagicMock()) as sp
        ):
            bm['chrome'].create_command = MagicMock(return_value = ['T', 'E', 'S' , 'T'])
            try:
                _browser.open('chrome', 'url', ['test1', 'test2'])
                self.assertEqual(sp.call_args.args[0], ['T', 'E', 'S' , 'T'])
            except Exception as e:
                self.fail()
    
    @patch('subprocess.Popen', MagicMock())
    def test_open_2(self):
        error_msg = '"edge" is not a supported browser.'
        
        try:
            _browser.open('edge', 'url', ['test1', 'test2'])
            self.fail()
        except Exception as e:
            self.assertIs(type(e), SupportError)
            self.assertEqual(e.args[0], error_msg)
