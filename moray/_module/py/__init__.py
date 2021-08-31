"""
呼び出される関数を管理
呼び出し用ESモジュール(JavaScript)の生成
"""

from jinja2 import PackageLoader, Environment

_expose_module = {}

def register(func):
    """
    デコレータ moray.expose の実装
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
    ファンクションを呼び出す
    
    Attributes:
        module (str): 呼び出すモジュール名
        func_name (str): 呼び出すファンクション名
        args (dict): 引数
    
    Returns:
        ファンクションの実行結果
    """
    
    func = _expose_module[module][func_name]
    return func(*args)

def render(module):
    """
    テンプレートからJavaScriptを生成
    
    Attributes:
        module (str): 呼び出すモジュール名
    
    Returns:
        str: 生成されたJavaScript
    """
    
    list_func_name = list(_expose_module[module].keys())
    
    loader = PackageLoader(package_name='moray._module.py', package_path='template')
    template = Environment(loader=loader).get_template(name='js_module.js')
    return template.render(module=module, list_func_name=list_func_name)
