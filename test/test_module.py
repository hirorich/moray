import json, unittest
from unittest.mock import patch, MagicMock

from moray import _module

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
        
        msg = {}
        msg[_module._METHOD] = _module._CALL
        msg = json.dumps(msg)
        
        with(
            patch('moray._module._called', MagicMock()) as cld,
            patch('moray._module._returned', side_effect = RuntimeError('_returned')) as rtd,
            patch('moray._module._exposed', side_effect = RuntimeError('_exposed')) as epd,
        ):
            _module.websocket_react(None, msg)
    
    def test_websocket_react_4(self):
        
        msg = {}
        msg[_module._METHOD] = _module._RETURN
        msg = json.dumps(msg)
        
        with(
            patch('moray._module._called', side_effect = RuntimeError('_called')) as cld,
            patch('moray._module._returned', MagicMock()) as rtd,
            patch('moray._module._exposed', side_effect = RuntimeError('_exposed')) as epd,
        ):
            _module.websocket_react(None, msg)
    
    def test_websocket_react_5(self):
        
        msg = {}
        msg[_module._METHOD] = _module._EXPOSE
        msg = json.dumps(msg)
        
        with(
            patch('moray._module._called', side_effect = RuntimeError('_called')) as cld,
            patch('moray._module._returned', side_effect = RuntimeError('_returned')) as rtd,
            patch('moray._module._exposed', MagicMock()) as epd,
        ):
            _module.websocket_react(None, msg)
    
    def test_websocket_react_6(self):
        error_msg = '"test" is not correct "method".'
        
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
                self.assertIs(type(e), RuntimeError)
                self.assertEqual(e.args[0], error_msg)
                return
            
            self.fail()
