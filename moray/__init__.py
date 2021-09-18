"""
moray初期化処理
morayが提供するAPIのInterface

ToDo:
    エラー処理デコレータ作成・テスト
    デフォルトログハンドラ: logging.getLogger('moray')
"""

import logging

from moray.exception import ConfigurationError

# ==================================================
# moray初期化処理
# ==================================================

class _CLASS():
    pass
js = _CLASS()

def _error_handle(logger, can_exit = False):
    """
    デコレータ
    エラー時にログを出力
    
    Attributes:
        logger (logging.Logger): ロガー
        can_exit (bool, optional): エラー時にアプリ終了
    
    Raises:
        ConfigurationError: チェックエラー
    
    ToDo:
        エラー時のアプリ終了
        テスト時のモック化
    """
    
    if not type(logger) is logging.Logger:
        raise ConfigurationError('"logger" is not "logging.Logger" type.')
    
    def impl(func):
        if not callable(func):
            raise ConfigurationError('"moray._error_handle" can only be used for "function".')
        
        def wrapper(*args, **dict):
            try:
                return func(*args, **dict)
            except Exception as e:
                logger.exception(e.args[0])
        return wrapper
    return impl

# ==================================================
# morayが提供するAPIのInterface
# ==================================================
from moray import _main

def run(*args, **dict):
    """
    moray起動
    
    Attributes:
        root (str): サーバのルートとなるフォルダ
        start_page (str, optional): 初期表示するページ
        host (str, optional): サーバのホスト
        port (int, optional): サーバのポート番号
        browser (str, optional): 使用するブラウザ
        cmdline_args (list<str>, optional): ブラウザの起動引数
        position (tuple<int, int>, optional): ブラウザを開いた際の位置
        size (tuple<int, int>, optional): ブラウザを開いた際のサイズ
    
    Raises:
        ConfigurationError: チェックエラー
    
    Examples:
        >>> import moray
        >>> moray.run(
                'web',
                start_page = 'index.html',
                host = 'localhost',
                port = 0,
                browser = 'chrome',
                cmdline_args = [],
                position = (480, 270),
                size = (960, 540)
            )
    """
    
    _main.run(*args, **dict)

def expose(func):
    """
    デコレータ
    JavaScriptから呼び出せるよう関数を公開
    
    Attributes:
        func (function): 登録する関数
    
    Raises:
        ConfigurationError: 型チェックエラー
    """
    
    return _main.expose(func)
