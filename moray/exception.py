"""
このモジュールで使用するユーザ定義例外

"""

class SupportError(RuntimeError):
    """
    サポート対象外のものに対する例外
    """
    
    pass

class MorayRuntimeError(RuntimeError):
    """
    moray内の例外
    """
    
    pass

