"""
moray初期化処理
morayが提供するAPIのInterface

ToDo:
    例外時のログ出力・終了処理のデコレータ
        loggerと終了可否は引数で受け取る
    デフォルトログハンドラ: logging.getLogger('moray')
"""

# ==================================================
# moray初期化処理
# ==================================================

class _CLASS():
    pass
js = _CLASS()

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
