import unittest
from unittest.mock import patch, MagicMock

import moray
from moray import _config
from moray._browser import chrome
from moray.exception import ConfigurationError, SupportError

@patch('moray._runner', MagicMock())
class MorayTest(unittest.TestCase):
    
    def init_config(self):
        _config.root = None
        _config.start_page = 'index.html'
        _config.browser = chrome.name
        _config.cmdline_args = []
        _config.position = None
        _config.size = None
        _config.host = 'localhost'
        _config.port = 0
    
    def test_run_1(self):
        
        self.init_config()
        
        try:
            moray.run('web')
        except Exception as e:
            self.fail()
