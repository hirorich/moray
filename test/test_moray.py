import logging, unittest
from unittest.mock import patch, MagicMock

import moray
from moray import _config
from moray._browser import chrome
from moray.exception import ConfigurationError, MorayRuntimeError

class Class():
    pass

def _FUNC():
    pass

def _FUNC_RAISE():
    raise Exception('test error')

_INT = 5
_FLOAT = 3.14
_STR = 'None'
_BOOL = True
_LIST = [1,2,3]
_TUPLE = (4,5,6)
_DICT = {'ABC': 'abc', 'XYZ': 789}
_CLASS = Class()

@patch('moray._runner', MagicMock())
class MorayTest_Run(unittest.TestCase):
    
    def init_config(self):
        _config.root = None
        _config.start_page = 'index.html'
        _config.browser = chrome.name
        _config.cmdline_args = []
        _config.position = None
        _config.size = None
        _config.host = 'localhost'
        _config.port = 0
    
    def test_run_root_1(self):
        
        self.init_config()
        
        for target in None, _INT, _FLOAT, _BOOL, _LIST, _TUPLE, _DICT, _CLASS, _FUNC, '', '   ', 'tests':
            try:
                moray.run(target)
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], e.__cause__.args[0])
                continue
            
            self.fail()
    
    def test_run_root_2(self):
        
        for target, correct in [
            ('web', 'web'),
            ('web  ', 'web'),
            ('  web', 'web'),
            ('  web  ', 'web')
        ]:
            self.init_config()
            
            try:
                moray.run(target)
                self.assertEqual(_config.root, correct)
            except Exception as e:
                self.fail()
    
    def test_run_start_page_1(self):
        
        self.init_config()
        
        for target in None, _INT, _FLOAT, _BOOL, _LIST, _TUPLE, _DICT, _CLASS, _FUNC:
            try:
                moray.run('web', start_page = target)
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], e.__cause__.args[0])
                continue
            
            self.fail()
    
    def test_run_start_page_2(self):
        
        self.init_config()
        
        for target, correct in [
            ('start_page.html', 'start_page.html'),
            ('start_page.html  ', 'start_page.html'),
            ('  start_page.html', 'start_page.html'),
            ('  start_page.html  ', 'start_page.html')
        ]:
            try:
                moray.run('web', start_page = target)
                self.assertEqual(_config.start_page, correct)
            except Exception as e:
                self.fail()
    
    def test_run_host_1(self):
        
        self.init_config()
        
        for target in None, _INT, _FLOAT, _BOOL, _LIST, _TUPLE, _DICT, _CLASS, _FUNC, '', '   ', 'tests':
            try:
                moray.run('web', host = target)
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], e.__cause__.args[0])
                continue
            
            self.fail()
    
    def test_run_host_2(self):
        
        for target, correct in [
            ('localhost', 'localhost'),
            ('125.32.46.0  ', '125.32.46.0'),
            ('  127.0.0.1', '127.0.0.1'),
            ('  localhost  ', 'localhost')
        ]:
            self.init_config()
            
            try:
                moray.run('web', host = target)
                self.assertEqual(_config.host, correct)
            except Exception as e:
                self.fail()
    
    def test_run_port_1(self):
        
        self.init_config()
        
        for target in None, _FLOAT, _STR, _BOOL, _LIST, _TUPLE, _DICT, _CLASS, _FUNC, -1, 1, 1023, 1024, 65536, 65537:
            try:
                moray.run('web', port = target)
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], e.__cause__.args[0])
                continue
            
            self.fail()
    
    def test_run_port_2(self):
        
        for target in 1025, 1026, 65534, 65535:
            self.init_config()
            
            try:
                moray.run('web', port = target)
                self.assertEqual(_config.port, target)
            except Exception as e:
                self.fail()
        
        self.init_config()
        
        try:
            moray.run('web', port = 0)
            self.assertNotEqual(_config.port, 0)
        except Exception as e:
            self.fail()
    
    def test_run_browser_1(self):
        
        self.init_config()
        
        for target in None, _INT, _FLOAT, _BOOL, _LIST, _TUPLE, _DICT, _CLASS, _FUNC:
            try:
                moray.run('web', browser = target)
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], e.__cause__.args[0])
                continue
            
            self.fail()
    
    def test_run_browser_2(self):
        
        self.init_config()
        
        for target in 'edge', 'safari':
            
            try:
                moray.run('web', browser = target)
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], e.__cause__.args[0])
                continue
            
            self.fail()
    
    def test_run_browser_3(self):
        
        for target, correct in [
            ('chrome', 'chrome'),
            ('chrome  ', 'chrome'),
            ('  chrome', 'chrome'),
            ('  chrome  ', 'chrome')
        ]:
            self.init_config()
            
            try:
                moray.run('web', browser = target)
                self.assertEqual(_config.browser, correct)
            except Exception as e:
                self.fail()
    
    def test_run_cmdline_args_1(self):
        
        self.init_config()
        
        for target in None, _INT, _FLOAT, _STR, _BOOL, _DICT, _CLASS, _FUNC, ('aaa'):
            try:
                moray.run('web', cmdline_args = target)
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], e.__cause__.args[0])
                continue
            
            self.fail()
    
    def test_run_cmdline_args_2(self):
        
        for target, correct in [
            ([], []),
            (['aaa'], ['aaa']),
            (['aaa', 'bbb'], ['aaa', 'bbb']),
            ((), []),
            (('aaa', ), ['aaa']),
            (('aaa', 'bbb'), ['aaa', 'bbb'])
        ]:
            self.init_config()
            
            try:
                moray.run('web', cmdline_args = target)
                self.assertEqual(_config.cmdline_args, correct)
            except Exception as e:
                self.fail()
    
    def test_run_position_1(self):
        
        self.init_config()
        
        for target in [
            _INT, _FLOAT, _STR, _BOOL, _DICT, _CLASS, _FUNC,
            [], [6184], [32, 165, 56], (), (69, ), (6, 65, 258),
            [32, '165'], ['32', 165], (65, '258'), ('65', 258)
        ]:
            try:
                moray.run('web', position = target)
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], e.__cause__.args[0])
                continue
            
            self.fail()
    
    def test_run_position_2(self):
        
        for target, correct in [
            (None, None),
            ([32, 165], (32, 165)),
            ((65, 258), (65, 258))
        ]:
            self.init_config()
            
            try:
                moray.run('web', position = target)
                self.assertEqual(_config.position, correct)
            except Exception as e:
                self.fail()
    
    def test_run_size_1(self):
        
        self.init_config()
        
        for target in [
            _INT, _FLOAT, _STR, _BOOL, _DICT, _CLASS, _FUNC,
            [], [6184], [32, 165, 56], (), (69, ), (6, 65, 258),
            [32, '165'], ['32', 165], (65, '258'), ('65', 258)
        ]:
            try:
                moray.run('web', size = target)
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], e.__cause__.args[0])
                continue
            
            self.fail()
    
    def test_run_size_2(self):
        
        for target, correct in [
            (None, None),
            ([32, 165], (32, 165)),
            ((65, 258), (65, 258))
        ]:
            self.init_config()
            
            try:
                moray.run('web', size = target)
                self.assertEqual(_config.size, correct)
            except Exception as e:
                self.fail()

@patch('moray.py.register', MagicMock())
class MorayTest_expose(unittest.TestCase):
    
    def test_expose_1(self):
        
        error_msg = '"moray.expose" can only be used for "function".'
        
        for target in None, _INT, _FLOAT, _STR, _BOOL, _LIST, _TUPLE, _DICT, _CLASS:
            try:
                moray.expose(target)
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
                continue
            
            self.fail()
    
    def test_expose_2(self):
        
        try:
            moray.expose(_FUNC)
        except Exception as e:
            self.fail()

@patch('moray.os._exit', MagicMock())
class MorayTest_error_handle(unittest.TestCase):
    
    def test_error_handle_1(self):
        
        error_msg = '"logger" is not "logging.Logger" type.'
        
        for target in None, _INT, _FLOAT, _STR, _BOOL, _LIST, _TUPLE, _DICT, _CLASS, _FUNC:
            try:
                moray._error_handle(target)
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
                continue
            
            self.fail()
    
    def test_error_handle_2(self):
        
        error_msg = '"can_exit" is not "bool" type.'
        logger = logging.getLogger(__name__)
        
        for target in None, _INT, _FLOAT, _STR, _LIST, _TUPLE, _DICT, _CLASS, _FUNC:
            try:
                moray._error_handle(logger, target)
            except Exception as e:
                self.assertIs(type(e), MorayRuntimeError)
                self.assertEqual(e.args[0], error_msg)
                continue
            
            self.fail()
    
    def test_error_handle_3(self):
        
        error_msg = '"moray._error_handle" can only be used for "function".'
        logger = logging.getLogger(__name__)
        
        for target in None, _INT, _FLOAT, _STR, _BOOL, _LIST, _TUPLE, _DICT, _CLASS:
            try:
                moray._error_handle(logger)(target)
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
                continue
            
            self.fail()
    
    def test_error_handle_4(self):
        
        logger = logging.getLogger(__name__)
        
        for func in _FUNC, _FUNC_RAISE:
            for target in True, False:
                try:
                    moray._error_handle(logger, target)(func)()
                except Exception as e:
                    self.fail()
    
    def test_error_handle_5(self):
        
        logger = logging.getLogger(__name__)
        
        for func in _FUNC, _FUNC_RAISE:
            try:
                moray._error_handle(logger)(func)()
            except Exception as e:
                self.fail()
