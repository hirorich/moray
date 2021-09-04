import json, unittest
from datetime import datetime
from unittest.mock import patch, MagicMock

from moray import _module
from moray.exception import MorayRuntimeError, MorayTimeoutError

class Class():
    pass

def _FUNC():
    pass

_INT = 5
_FLOAT = 3.14
_STR = 'None'
_BOOL = True
_LIST = [1,2,3]
_TUPLE = (4,5,6)
_DICT = {'ABC': 'abc', 'XYZ': 789}
_CLASS = Class()

class ModuleTest(unittest.TestCase):
    
    def test_websocket_react_1(self):
        msg = 'aa:123'
        
        with(
            patch('moray._module._called', MagicMock()) as cld,
            patch('moray._module._returned', MagicMock()) as rtd,
            patch('moray._module._exposed', MagicMock()) as epd,
        ):
            try:
                _module.websocket_react(None, msg)
            except Exception as e:
                return
            
            self.fail()
    
    def test_websocket_react_2(self):
        msg = {}
        msg['sample'] = 'test'
        msg = json.dumps(msg)
        
        with(
            patch('moray._module._called', MagicMock()) as cld,
            patch('moray._module._returned', MagicMock()) as rtd,
            patch('moray._module._exposed', MagicMock()) as epd,
        ):
            try:
                _module.websocket_react(None, msg)
            except Exception as e:
                return
            
            self.fail()
    
    def test_websocket_react_3(self):
        error_msg = '"{0}" is not "str" type.'.format(_module._METHOD)
        
        with(
            patch('moray._module._called', MagicMock()) as cld,
            patch('moray._module._returned', MagicMock()) as rtd,
            patch('moray._module._exposed', MagicMock()) as epd,
        ):
            for target in None, _INT, _FLOAT, _BOOL, _LIST, _TUPLE, _DICT:
                msg = {}
                msg[_module._METHOD] = target
                msg = json.dumps(msg)
                
                try:
                    _module.websocket_react(None, msg)
                except Exception as e:
                    self.assertIs(type(e), MorayRuntimeError)
                    self.assertEqual(e.args[0], error_msg)
                    continue
                
                self.fail()
    
    def test_websocket_react_4(self):
        
        msg = {}
        msg[_module._METHOD] = _module._CALL
        msg = json.dumps(msg)
        
        with(
            patch('moray._module._called', MagicMock()) as cld,
            patch('moray._module._returned', side_effect = RuntimeError('_returned')) as rtd,
            patch('moray._module._exposed', side_effect = RuntimeError('_exposed')) as epd,
        ):
            _module.websocket_react(None, msg)
    
    def test_websocket_react_5(self):
        
        msg = {}
        msg[_module._METHOD] = _module._RETURN
        msg = json.dumps(msg)
        
        with(
            patch('moray._module._called', side_effect = RuntimeError('_called')) as cld,
            patch('moray._module._returned', MagicMock()) as rtd,
            patch('moray._module._exposed', side_effect = RuntimeError('_exposed')) as epd,
        ):
            _module.websocket_react(None, msg)
    
    def test_websocket_react_6(self):
        
        msg = {}
        msg[_module._METHOD] = _module._EXPOSE
        msg = json.dumps(msg)
        
        with(
            patch('moray._module._called', side_effect = RuntimeError('_called')) as cld,
            patch('moray._module._returned', side_effect = RuntimeError('_returned')) as rtd,
            patch('moray._module._exposed', MagicMock()) as epd,
        ):
            _module.websocket_react(None, msg)
    
    def test_websocket_react_7(self):
        error_msg = 'not correct "method".'
        
        msg = {}
        msg[_module._METHOD] = 'test'
        msg = json.dumps(msg)
        
        with(
            patch('moray._module._called', MagicMock()) as cld,
            patch('moray._module._returned', MagicMock()) as rtd,
            patch('moray._module._exposed', MagicMock()) as epd,
        ):
            try:
                _module.websocket_react(None, msg)
            except Exception as e:
                self.assertIs(type(e), MorayRuntimeError)
                self.assertEqual(e.args[0], error_msg)
                return
            
            self.fail()
    
    @patch('moray._module._call_py_func', MagicMock(return_value = ('result', True)))
    def test_called_1(self):
        parsed_msg = {}
        parsed_msg[_module._ID] = 'id'
        parsed_msg[_module._MODULE] = 'module'
        parsed_msg[_module._FUNC_NAME] = 'func_name'
        parsed_msg[_module._ARGS] = ('arg0', 'arg1')
        
        return_msg = {}
        return_msg[_module._ID] = 'id'
        return_msg[_module._RETURN] = True
        return_msg[_module._RESULT] = 'result'
        return_msg[_module._IS_SUCCESS] = True
        return_msg = json.dumps(return_msg)
        
        ws = MagicMock()
        
        try:
            _module._called(ws, parsed_msg)
            args, kwargs = ws.send.call_args
            self.assertEqual(args[0], return_msg)
            
            parsed_msg[_module._ARGS] = ['arg0', 'arg1']
            _module._called(ws, parsed_msg)
            args, kwargs = ws.send.call_args
            self.assertEqual(args[0], return_msg)
        except Exception as e:
            self.fail()
    
    @patch('moray._module._call_py_func', MagicMock(return_value = ('result', True)))
    def test_called_2(self):
        parsed_msg = {}
        #parsed_msg[_module._ID] = 'id'
        parsed_msg[_module._MODULE] = 'module'
        parsed_msg[_module._FUNC_NAME] = 'func_name'
        parsed_msg[_module._ARGS] = ('arg0', 'arg1')
        
        ws = MagicMock()
        
        try:
            _module._called(ws, parsed_msg)
        except Exception as e:
            return
        
        self.fail()
    
    @patch('moray._module._call_py_func', MagicMock(return_value = ('result', True)))
    def test_called_3(self):
        error_msg = '"{0}" is not "str" type.'.format(_module._ID)
        
        ws = MagicMock()
        
        for target in None, _INT, _FLOAT, _BOOL, _LIST, _TUPLE, _DICT:
            parsed_msg = {}
            parsed_msg[_module._ID] = target
            parsed_msg[_module._MODULE] = 'module'
            parsed_msg[_module._FUNC_NAME] = 'func_name'
            parsed_msg[_module._ARGS] = ('arg0', 'arg1')
            
            try:
                _module._called(ws, parsed_msg)
            except Exception as e:
                self.assertIs(type(e), MorayRuntimeError)
                self.assertEqual(e.args[0], error_msg)
                continue
            
            self.fail()
    
    @patch('moray._module._call_py_func', MagicMock(return_value = ('result', True)))
    def test_called_4(self):
        parsed_msg = {}
        parsed_msg[_module._ID] = 'id'
        #parsed_msg[_module._MODULE] = 'module'
        parsed_msg[_module._FUNC_NAME] = 'func_name'
        parsed_msg[_module._ARGS] = ('arg0', 'arg1')
        
        ws = MagicMock()
        
        try:
            _module._called(ws, parsed_msg)
        except Exception as e:
            return
        
        self.fail()
    
    @patch('moray._module._call_py_func', MagicMock(return_value = ('result', True)))
    def test_called_5(self):
        error_msg = '"{0}" is not "str" type.'.format(_module._MODULE)
        
        ws = MagicMock()
        
        for target in None, _INT, _FLOAT, _BOOL, _LIST, _TUPLE, _DICT:
            parsed_msg = {}
            parsed_msg[_module._ID] = 'id'
            parsed_msg[_module._MODULE] = target
            parsed_msg[_module._FUNC_NAME] = 'func_name'
            parsed_msg[_module._ARGS] = ('arg0', 'arg1')
            
            try:
                _module._called(ws, parsed_msg)
            except Exception as e:
                self.assertIs(type(e), MorayRuntimeError)
                self.assertEqual(e.args[0], error_msg)
                continue
            
            self.fail()
    
    @patch('moray._module._call_py_func', MagicMock(return_value = ('result', True)))
    def test_called_6(self):
        parsed_msg = {}
        parsed_msg[_module._ID] = 'id'
        parsed_msg[_module._MODULE] = 'module'
        #parsed_msg[_module._FUNC_NAME] = 'func_name'
        parsed_msg[_module._ARGS] = ('arg0', 'arg1')
        
        ws = MagicMock()
        
        try:
            _module._called(ws, parsed_msg)
        except Exception as e:
            return
        
        self.fail()
    
    @patch('moray._module._call_py_func', MagicMock(return_value = ('result', True)))
    def test_called_7(self):
        error_msg = '"{0}" is not "str" type.'.format(_module._FUNC_NAME)
        
        ws = MagicMock()
        
        for target in None, _INT, _FLOAT, _BOOL, _LIST, _TUPLE, _DICT:
            parsed_msg = {}
            parsed_msg[_module._ID] = 'id'
            parsed_msg[_module._MODULE] = 'module'
            parsed_msg[_module._FUNC_NAME] = target
            parsed_msg[_module._ARGS] = ('arg0', 'arg1')
            
            try:
                _module._called(ws, parsed_msg)
            except Exception as e:
                self.assertIs(type(e), MorayRuntimeError)
                self.assertEqual(e.args[0], error_msg)
                continue
            
            self.fail()
    
    @patch('moray._module._call_py_func', MagicMock(return_value = ('result', True)))
    def test_called_8(self):
        parsed_msg = {}
        parsed_msg[_module._ID] = 'id'
        parsed_msg[_module._MODULE] = 'module'
        parsed_msg[_module._FUNC_NAME] = 'func_name'
        #parsed_msg[_module._ARGS] = ('arg0', 'arg1')
        
        ws = MagicMock()
        
        try:
            _module._called(ws, parsed_msg)
        except Exception as e:
            return
        
        self.fail()
    
    @patch('moray._module._call_py_func', MagicMock(return_value = ('result', True)))
    def test_called_9(self):
        error_msg = '"{0}" is not "list" or "tuple" type.'.format(_module._ARGS)
        
        ws = MagicMock()
        
        for target in None, _INT, _FLOAT, _STR, _BOOL, _DICT:
            parsed_msg = {}
            parsed_msg[_module._ID] = 'id'
            parsed_msg[_module._MODULE] = 'module'
            parsed_msg[_module._FUNC_NAME] = 'func_name'
            parsed_msg[_module._ARGS] = target
            
            try:
                _module._called(ws, parsed_msg)
            except Exception as e:
                self.assertIs(type(e), MorayRuntimeError)
                self.assertEqual(e.args[0], error_msg)
                continue
            
            self.fail()
    
    def test_called_10(self):
        parsed_msg = {}
        parsed_msg[_module._ID] = 'id'
        parsed_msg[_module._MODULE] = 'module'
        parsed_msg[_module._FUNC_NAME] = 'func_name'
        parsed_msg[_module._ARGS] = ('arg0', 'arg1')
        
        ws = MagicMock()
        
        for target in None, _INT, _FLOAT, _STR, _BOOL, _LIST, _TUPLE, _DICT:
            with patch('moray._module._call_py_func', MagicMock(return_value = (target, True))) as cpf:
                try:
                    _module._called(ws, parsed_msg)
                except Exception as e:
                    self.fail()
    
    def test_called_11(self):
        parsed_msg = {}
        parsed_msg[_module._ID] = 'id'
        parsed_msg[_module._MODULE] = 'module'
        parsed_msg[_module._FUNC_NAME] = 'func_name'
        parsed_msg[_module._ARGS] = ('arg0', 'arg1')
        
        ws = MagicMock()
        
        for target in _FUNC, _CLASS:
            with patch('moray._module._call_py_func', MagicMock(return_value = (target, True))) as cpf:
                try:
                    _module._called(ws, parsed_msg)
                except Exception as e:
                    continue
                
                self.fail()
    
    def test_returned_1(self):
        parsed_msg = {}
        parsed_msg[_module._ID] = 'id'
        parsed_msg[_module._IS_SUCCESS] = True
        parsed_msg[_module._RESULT] = 'result'
        
        try:
            _module._returned(parsed_msg)
            result = _module._call_result['id']
            self.assertEqual(result[_module._IS_SUCCESS], True)
            self.assertEqual(result[_module._RESULT], 'result')
        except Exception as e:
            self.fail()
    
    def test_returned_2(self):
        parsed_msg = {}
        #parsed_msg[_module._ID] = 'id'
        parsed_msg[_module._IS_SUCCESS] = True
        parsed_msg[_module._RESULT] = 'result'
        
        try:
            _module._returned(parsed_msg)
        except Exception as e:
            return
        
        self.fail()
    
    def test_returned_3(self):
        error_msg = '"{0}" is not "str" type.'.format(_module._ID)
        
        for target in None, _INT, _FLOAT, _BOOL, _LIST, _TUPLE, _DICT:
            parsed_msg = {}
            parsed_msg[_module._ID] = target
            parsed_msg[_module._IS_SUCCESS] = True
            parsed_msg[_module._RESULT] = 'result'
            
            try:
                _module._returned(parsed_msg)
            except Exception as e:
                self.assertIs(type(e), MorayRuntimeError)
                self.assertEqual(e.args[0], error_msg)
                continue
            
            self.fail()
    
    def test_returned_4(self):
        parsed_msg = {}
        parsed_msg[_module._ID] = 'id'
        #parsed_msg[_module._IS_SUCCESS] = True
        parsed_msg[_module._RESULT] = 'result'
        
        try:
            _module._returned(parsed_msg)
        except Exception as e:
            return
        
        self.fail()
    
    def test_returned_5(self):
        error_msg = '"{0}" is not "bool" type.'.format(_module._IS_SUCCESS)
        
        for target in None, _INT, _FLOAT, _STR, _LIST, _TUPLE, _DICT:
            parsed_msg = {}
            parsed_msg[_module._ID] = 'id'
            parsed_msg[_module._IS_SUCCESS] = target
            parsed_msg[_module._RESULT] = 'result'
            
            try:
                _module._returned(parsed_msg)
            except Exception as e:
                self.assertIs(type(e), MorayRuntimeError)
                self.assertEqual(e.args[0], error_msg)
                continue
            
            self.fail()
    
    def test_returned_6(self):
        parsed_msg = {}
        parsed_msg[_module._ID] = 'id'
        parsed_msg[_module._IS_SUCCESS] = True
        #parsed_msg[_module._RESULT] = 'result'
        
        try:
            _module._returned(parsed_msg)
        except Exception as e:
            return
        
        self.fail()
    
    def test_returned_7(self):
        error_msg = '"{0}" is not "str" type.'.format(_module._RESULT)
        
        for target in None, _INT, _FLOAT, _BOOL, _LIST, _TUPLE, _DICT:
            parsed_msg = {}
            parsed_msg[_module._ID] = 'id'
            parsed_msg[_module._IS_SUCCESS] = True
            parsed_msg[_module._RESULT] = target
            
            try:
                _module._returned(parsed_msg)
            except Exception as e:
                self.assertIs(type(e), MorayRuntimeError)
                self.assertEqual(e.args[0], error_msg)
                continue
            
            self.fail()
    
    @patch('moray._module._create_js_func', MagicMock())
    def test_exposed_1(self):
        parsed_msg = {}
        parsed_msg[_module._FUNC_NAME] = 'func_name'
        
        with patch('moray._module.moray.js', MagicMock()) as moray_js:
            try:
                _module._exposed(None, parsed_msg)
                if not 'func_name' in moray_js.__dict__:
                    self.fail()
            except Exception as e:
                self.fail()
    
    @patch('moray._module._create_js_func', MagicMock())
    def test_exposed_2(self):
        parsed_msg = {}
        #parsed_msg[_module._FUNC_NAME] = 'func_name'
        
        with patch('moray._module.moray.js', MagicMock()) as moray_js:
            try:
                _module._exposed(None, parsed_msg)
            except Exception as e:
                return
        
        self.fail()
    
    @patch('moray._module._create_js_func', MagicMock())
    def test_exposed_3(self):
        error_msg = '"{0}" is not "str" type.'.format(_module._FUNC_NAME)
        
        for target in None, _INT, _FLOAT, _BOOL, _LIST, _TUPLE, _DICT:
            parsed_msg = {}
            parsed_msg[_module._FUNC_NAME] = target
            
            with patch('moray._module.moray.js', MagicMock()) as moray_js:
                try:
                    _module._exposed(None, parsed_msg)
                except Exception as e:
                    self.assertIs(type(e), MorayRuntimeError)
                    self.assertEqual(e.args[0], error_msg)
                    continue
            
            self.fail()
    
    @patch('moray._module.py.call', MagicMock(return_value = 'return_value'))
    def test_call_py_func_1(self):
        result, is_success = _module._call_py_func(None, None, None)
        self.assertEqual(result, 'return_value')
        self.assertEqual(is_success, True)
    
    @patch('moray._module.py.call', MagicMock(side_effect = RuntimeError('return_value')))
    def test_call_py_func_2(self):
        result, is_success = _module._call_py_func(None, None, None)
        self.assertEqual(result, 'calling python function is faild.')
        self.assertEqual(is_success, False)
    
    @patch('moray._module._uniqueId', MagicMock(return_value = 'uniqueId'))
    @patch('moray._module.time.sleep', MagicMock())
    def test_create_js_func_1(self):
        ws = MagicMock()
        func_name = 'func_name'
        
        call_msg = {}
        call_msg[_module._ID] = 'uniqueId'
        call_msg[_module._RETURN] = False
        call_msg[_module._FUNC_NAME] = func_name
        call_msg[_module._ARGS] = ('abc', 123)
        call_msg = json.dumps(call_msg)
        
        _module._call_result['uniqueId'] = {
            _module._IS_SUCCESS: True,
            _module._RESULT: 'result'
        }
        
        try:
            call_js = _module._create_js_func(ws, func_name)
            get_result = call_js('abc', 123)
            result = get_result()
        except Exception as e:
            self.fail()
        
        args, kwargs = ws.send.call_args
        self.assertEqual(args[0], call_msg)
        self.assertEqual(result, 'result')
    
    @patch('moray._module._uniqueId', MagicMock(return_value = 'uniqueId'))
    @patch('moray._module.time.sleep', MagicMock())
    def test_create_js_func_2(self):
        ws = MagicMock()
        func_name = 'func_name'
        
        error_msg = 'result'
        
        _module._call_result['uniqueId'] = {
            _module._IS_SUCCESS: False,
            _module._RESULT: 'result'
        }
        
        try:
            call_js = _module._create_js_func(ws, func_name)
            get_result = call_js('abc', 123)
            result = get_result()
        except Exception as e:
            self.assertIs(type(e), MorayRuntimeError)
            self.assertEqual(e.args[0], error_msg)
            return
        
        self.fail()
    
    @patch('moray._module._uniqueId', MagicMock(return_value = 'uniqueId'))
    @patch('moray._module.time.sleep', MagicMock())
    def test_create_js_func_3(self):
        ws = MagicMock()
        func_name = 'func_name'
        
        error_msg = 'Could not receive execution results from JavaScript.'
        
        if 'uniqueId' in _module._call_result:
            del _module._call_result['uniqueId']
        
        try:
            call_js = _module._create_js_func(ws, func_name)
            get_result = call_js('abc', 123)
            result = get_result()
        except Exception as e:
            self.assertIs(type(e), MorayTimeoutError)
            self.assertEqual(e.args[0], error_msg)
            return
        
        self.fail()
    
    def test_uniqueId_1(self):
        test_datetime = datetime(2021, 2, 3, 4, 5, 6, 789)
        test_random = 0.123
        strong = 1000
        result = hex(int(test_datetime.timestamp() * 1000))[2:] + hex(int(test_random * strong))[2:]
        with (
            patch('moray._module.datetime', MagicMock()) as dt,
            patch('moray._module.datetime.now', MagicMock(return_value = test_datetime)) as dtn,
            patch('moray._module.random.random', MagicMock(return_value = test_random)) as rr
        ):
            self.assertEqual(_module._uniqueId(), result)
    
    def test_uniqueId_2(self):
        test_datetime = datetime(2021, 2, 3, 4, 5, 6, 789)
        test_random = 0.123
        strong = 500
        result = hex(int(test_datetime.timestamp() * 1000))[2:] + hex(int(test_random * strong))[2:]
        with (
            patch('moray._module.datetime', MagicMock()) as dt,
            patch('moray._module.datetime.now', MagicMock(return_value = test_datetime)) as dtn,
            patch('moray._module.random.random', MagicMock(return_value = test_random)) as rr
        ):
            self.assertEqual(_module._uniqueId(strong), result)
