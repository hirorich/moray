"""
このモジュールで使用するユーザ定義例外

"""

class SupportError(RuntimeError):
    """
    サポート対象外のものに対する例外
    
    """
    
    pass

class ConfigurationError(RuntimeError):
    """
    設定に関する例外
    
    """
    
    pass

