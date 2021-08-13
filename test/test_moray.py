from pathlib import Path
import unittest
from unittest.mock import patch, MagicMock

import moray
from moray import _config
from moray._browser import chrome
from moray.exception import ConfigurationError, SupportError

class Class():
    pass

_INT = 5
_FLOAT = 3.14
_STR = 'None'
_BOOL = True
_LIST = [1,2,3]
_TUPLE = (4,5,6)
_DICT = {'ABC': 'abc', 'XYZ': 789}
_CLASS = Class()

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
    
    def test_check_not_None_1(self):
        
        for target in _INT, _FLOAT, _STR, _BOOL, _LIST, _TUPLE, _DICT, _CLASS:
            try:
                moray._check_not_None(target, 'aaa')
            except Exception as e:
                self.fail()
    
    def test_check_not_None_2(self):
        error_msg = '"aaa" is None.'
        
        try:
            moray._check_not_None(None, 'aaa')
            self.fail()
        except Exception as e:
            self.assertIs(type(e), ConfigurationError)
            self.assertEqual(e.args[0], error_msg)
    
    def test_check_str_1(self):
        
        try:
            moray._check_str(_STR, 'aaa')
        except Exception as e:
            self.fail()
    
    def test_check_str_2(self):
        error_msg = '"aaa" is not "str" type.'
        
        for target in None, _INT, _FLOAT, _BOOL, _LIST, _TUPLE, _DICT, _CLASS:
            try:
                moray._check_str(target, 'aaa')
                self.fail()
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_check_int_1(self):
        
        try:
            moray._check_int(_INT, 'aaa')
        except Exception as e:
            self.fail()
    
    def test_check_int_2(self):
        error_msg = '"aaa" is not "int" type.'
        
        for target in None, _FLOAT, _STR, _BOOL, _LIST, _TUPLE, _DICT, _CLASS:
            try:
                moray._check_int(target, 'aaa')
                self.fail()
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_check_list_or_tuple_1(self):
        
        for target in _LIST, _TUPLE:
            try:
                moray._check_list_or_tuple(target, 'aaa')
            except Exception as e:
                self.fail()
    
    def test_check_list_or_tuple_2(self):
        error_msg = '"aaa" is not "list" or "tuple" type.'
        
        for target in None, _INT, _FLOAT, _STR, _BOOL, _DICT, _CLASS:
            try:
                moray._check_list_or_tuple(target, 'aaa')
                self.fail()
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_check_not_whitespace_1(self):
        
        for target in 'abc', ' 13', 'tgd  ', '  xy  sd   ':
            try:
                moray._check_not_whitespace(target, 'aaa')
            except Exception as e:
                self.fail()
    
    def test_check_not_whitespace_2(self):
        error_msg = '"aaa" is whitespace.'
        
        for target in '', ' ', '         ':
            try:
                moray._check_not_whitespace(target, 'aaa')
                self.fail()
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_check_exist_1(self):
        
        for target in 'web', 'moray/_browser  ', r'  moray\_browser':
            try:
                moray._check_exist(target)
            except Exception as e:
                self.fail()
    
    def test_check_exist_2(self):
        
        for target in 'webs', 'moray/browser', r'moray\browser':
            value = Path(target.strip(' '))
            error_msg = '"{0}" is not exist.'.format(str(value))
            try:
                moray._check_exist(target)
                self.fail()
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_check_2_int_list_or_tuple_1(self):
        
        for target in [1, 6], (849, 51):
            try:
                moray._check_2_int_list_or_tuple(target, 'aaa')
            except Exception as e:
                self.fail()
    
    def test_check_2_int_list_or_tuple_2(self):
        error_msg = '"aaa" has only 2 "int" type.'
        
        for target in [], [6184], [1, 6, 56], (), (69, ), (6, 849, 51):
            try:
                moray._check_2_int_list_or_tuple(target, 'aaa')
                self.fail()
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_check_2_int_list_or_tuple_3(self):
        error_msg = '"aaa" has only 2 "int" type.'
        
        for target in [1, '6'], ['1', 6], (849, '51'), ('849', 51):
            try:
                moray._check_2_int_list_or_tuple(target, 'aaa')
                self.fail()
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_check_host_1(self):
        
        for target in 'localhost', '0.0.0.0', '255.255.255.255':
            try:
                moray._check_host(target)
            except Exception as e:
                self.fail()
    
    def test_check_host_2(self):
        error_msg = '"host" is not "localhost" or "xxx.xxx.xxx.xxx".(0 <= xxx <= 255)'
        
        for target in 'LOCALHOST', 'a.0.0.0', '0.0.0':
            try:
                moray._check_host(target)
                self.fail()
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_check_host_3(self):
        error_msg = '"host" is not "localhost" or "xxx.xxx.xxx.xxx".(0 <= xxx <= 255)'
        
        for target in '-1.0.0.0', '0.-1.0.0', '0.0.-1.0', '0.0.0.-1', '256.255.255.255', '255.256.255.255', '255.255.256.255', '255.255.255.256':
            try:
                moray._check_host(target)
                self.fail()
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_check_port_1(self):
        
        for target in 0, 1, 65534, 65535:
            try:
                moray._check_port(target)
            except Exception as e:
                self.fail()
    
    def test_check_port_2(self):
        error_msg = '"port" is less than 0 or greater than 65535.'
        
        for target in -2, -1, 65536, 65537:
            try:
                moray._check_port(target)
                self.fail()
            except Exception as e:
                self.assertIs(type(e), ConfigurationError)
                self.assertEqual(e.args[0], error_msg)
    
    def test_run_1(self):
        
        self.init_config()
        
        try:
            moray.run('web')
        except Exception as e:
            self.fail()

