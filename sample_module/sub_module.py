"""
expose機能の検証用
"""

import moray

@moray.expose
def get_module_name():
    """
    モジュール名取得
    
    Return:
        モジュール名
    """
    
    return __name__

@moray.expose
def sum(a, b):
    """
    合計算出
    
    Attributes:
        a (int): 入力値1
        b (int): 入力値2
    
    Return:
        入力値の合計
    """
    
    return a + b

@moray.expose
def sum_list(items):
    """
    合計算出(リスト)
    
    Attributes:
        items (list<int>): 入力値リスト
    
    Return:
        入力値の合計
    """
    
    result = 0
    for item in items:
        result += item
    
    return result

@moray.expose
def log_msg():
    print('start: log_msg')
    result = moray.js.log_msg('Python: exposed')()
    print(result)
    print('end: log_msg')

@moray.expose
def log_msg2():
    print('start: log_msg2')
    try:
        result = moray.js.log_msg2('Python: exposed')()
        print(result)
        print('end: log_msg2')
    except Exception as e:
        r = '{0} {1}'.format(type(e), e.args[0])
        print(r)
        return r

@moray.expose
def return_two(a, b):
    """
    複数返却
    
    Attributes:
        a (int): 入力値1
        b (int): 入力値2
    
    Return:
        b (int): 入力値2
        a (int): 入力値1
    """
    
    return b, a

@moray.expose
def return_list():
    """
    リスト返却
    
    Return:
        list: リスト返却値
    """
    
    return [1, 2, 3]

@moray.expose
def return_tuple():
    """
    タプル返却
    
    Return:
        list: タプル返却値
    """
    
    return (4, 5, 6)

@moray.expose
def raise_py_exception():
    raise RuntimeError('Python Error')

@moray.expose
def raise_js_exception():
    try:
        moray.js.raise_js_exception()()
    except Exception as e:
        print(e.args[0])
        raise

def not_expose():
    """
    expose対象外関数
    """
    
    raise RuntimeError('expose対象外関数')

