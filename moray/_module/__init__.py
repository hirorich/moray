import json

import moray
from moray._module import py, js

_RETURN = 'return'
_CALL = 'call'
_EXPOSE = 'expose'

def websocket_react(ws, msg):
    
    print(msg)
    parsed_msg = json.loads(msg)
    method = parsed_msg['method']
    
    if method == _CALL:
        print(_CALL)
        id = parsed_msg['id']
        module = parsed_msg['module']
        func_name = parsed_msg['func_name']
        args = parsed_msg['args']
        
        result, is_success = _call_py_func(module, func_name, args)
        
        return_msg = {}
        return_msg['id'] = id
        return_msg['return'] = True
        return_msg['result'] = result
        return_msg['is_success'] = is_success
        
        ws.send(json.dumps(return_msg))
        
    elif method == _RETURN:
        print(_RETURN)
        id = parsed_msg['id']
        result = parsed_msg['result']
        is_success = parsed_msg['is_success']
        js._call_result[id] = result
        
    elif method == _EXPOSE:
        print(_EXPOSE)
        func_name = parsed_msg['func_name']
        moray.js.__setattr__(func_name, js.create_js_func(ws, func_name))
        print(func_name)

def _call_py_func(module, func_name, args):
    """
    exposeしたファンクションを呼び出す
    
    Attributes:
        module (str): 呼び出すモジュール名
        func_name (str): 呼び出すファンクション名
        args (dict): 引数
    
    Returns:
        ファンクションの実行結果
        実行成否(True:成功, False:失敗)
    """
    
    try:
        result = py.call(module, func_name, args)
        return result, True
    except:
        # ToDo: ログ出力
        result = 'calling python function is faild.'
        return result, False
