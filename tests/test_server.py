import unittest
from unittest.mock import patch

from moray import _server

def raise_mock(arg):
    raise

@patch('moray._server._logger.exception', raise_mock)
class ServerTest(unittest.TestCase):
    
    def test_generate_port_1(self):
        
        self.assertNotEqual(_server.generate_port(0), 0)
    
    def test_generate_port_2(self):
        
        self.assertEqual(_server.generate_port(6000), 6000)
    
    @patch('moray._server._config.port', 5500)
    @patch('moray._server._config.start_page', 'aaa.xxx')
    def test_generate_start_url_1(self):
        
        correct = 'http://localhost:5500/aaa.xxx'
        self.assertEqual(_server.generate_start_url(), correct)
    
    @patch('moray._server._config.port', 4500)
    def test_generate_confirm_running_url_1(self):
        
        correct = 'http://localhost:4500/moray/confirm_running'
        self.assertEqual(_server.generate_confirm_running_url(), correct)
