"""
フォルダをモジュール化するために配置

"""

import json, random, time
from datetime import datetime

_call_result = {}

def uniqueId(strong = 1000):
    return hex(int(datetime.now().timestamp() * 1000))[2:] + hex(int(random.random() * strong))[2:]

def create_js_func(ws, func_name):
    def call_js(*args):
        id = uniqueId()
        
        call_msg = {}
        call_msg['id'] = id
        call_msg['return'] = False
        call_msg['func_name'] = func_name
        call_msg['args'] = args
        
        ws.send(json.dumps(call_msg))
        
        def get_result():
            for i in range(10):
                if id in _call_result:
                    return _call_result[id]
                
                time.sleep(1)
            
            raise RuntimeError('time out')
        
        return get_result
    
    return call_js
