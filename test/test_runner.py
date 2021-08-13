import unittest
from unittest.mock import patch, MagicMock
from requests.exceptions import Timeout

from moray import _runner

@patch('moray._runner._browser', MagicMock())
@patch('moray._runner._server', MagicMock())
class RunnerTest(unittest.TestCase):
    
    @patch('requests.get', MagicMock(return_value = MagicMock(ok = True)))
    def test_open_browser_1(self):
        
        try:
            _runner.open_browser()
        except Exception as e:
            self.fail()
    
    @patch('requests.get', MagicMock(return_value = MagicMock(ok = False)))
    def test_open_browser_2(self):
        error_msg = 'Could not confirm server run.'
        
        try:
            _runner.open_browser()
            self.fail()
        except Exception as e:
            self.assertIs(type(e), RuntimeError)
            self.assertEqual(e.args[0], error_msg)
    
    @patch('requests.get', MagicMock(side_effect = Timeout('TimeOut Error')))
    def test_open_browser_3(self):
        error_msg = 'TimeOut Error'
        
        try:
            _runner.open_browser()
            self.fail()
        except Exception as e:
            self.assertIs(type(e), Timeout)
            self.assertEqual(e.args[0], error_msg)