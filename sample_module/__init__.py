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
    
    return 'sample_module'

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

def not_expose():
    """
    expose対象外関数
    """
    
    raise RuntimeError('expose対象外関数')

