_expose_module = {}

def register(func):
    """
    デコレータ
    JavaScriptから呼び出すファンクションを登録
    
    Attributes:
        func (function): 登録するファンクション
    """

    module = func.__module__
    func_name = func.__name__
    
    _expose_module.setdefault(module, {})
    _expose_module[module][func_name] = func

def call(module, func_name, args):
    """
    JavaScriptから呼び出すファンクションを登録
    
    Attributes:
        module (str): 呼び出すモジュール名
        func_name (str): 呼び出すファンクション名
        args (dict): 引数
    """
    
    func = _expose_module[module][func_name]
    return func(*args)
