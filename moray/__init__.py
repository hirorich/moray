"""
morayが提供するAPIのInterface

"""

from moray import config, const, browser
from moray.exception import ConfigurationError, SupportError
from pathlib import Path
import re

def init(root, **kwargs):
    """
    morayライブラリの初期化
    
    Attributes:
        root (str): サーバのルートとなるフォルダ
        start_page (str, optional): 初期表示するページ
        browser (str, optional): 使用するブラウザ
        cmdline_args (list<str>, optional): ブラウザの起動引数
        position (tuple<int, int>, optional): ブラウザを開いた際の位置
        size (tuple<int, int>, optional): ブラウザを開いた際のサイズ
    
    """
    
    # Noneを指定された項目を排除
    args = dict(
        filter(
            lambda item: item[1] is not None, kwargs.items()
        )
    )
    
    # ROOTの値設定
    if root is None or root.strip(' ') == '':
        msg = '"' + const.ROOT + '" is unspecified or whitespace.'
        raise ConfigurationError(msg)
    config.root = root.strip(' ')
    
    # ROOTフォルダの存在チェック
    root_path = Path(config.root)
    if not root_path.exists():
        msg = '"' + str(root_path) + '" is not exist.'
        raise ConfigurationError(msg)
    
    # START_PAGEの値設定
    if const.START_PAGE in args:
        start_page = args[const.START_PAGE]
        if start_page is None or start_page.strip(' ') == '':
            config.start_page = 'index.html'
        else:
            config.start_page = start_page.strip(' ')
    
    # ROOT/START_PAGEの存在チェック
    start_path = root_path.joinpath(config.start_page)
    if not start_path.exists():
        msg = '"' + str(start_path) + '" is not exist.'
        raise ConfigurationError(msg)
    
    # ブラウザの値設定
    if const.BROWSER in args:
        config.browser = args[const.BROWSER].strip(' ')
    
    # ブラウザのサポートチェック
    if not browser.is_supported(config.browser):
        msg = '"' + config.browser + '" is not a supported browser.'
        raise SupportError(msg)
    
    # CMDLINE_ARGSの型チェック
    if const.CMDLINE_ARGS in args:
        if not type(args[const.CMDLINE_ARGS]) is list:
            msg = '"' + const.CMDLINE_ARGS + '" is not list.'
            raise ConfigurationError(msg)
        config.cmdline_args.update(args[const.CMDLINE_ARGS])
    
    # POSITIONの型チェック
    if const.POSITION in args:
        if not type(args[const.POSITION]) is tuple:
            msg = '"' + const.POSITION + '" is not tuple.'
            raise ConfigurationError(msg)
        elif len(args[const.POSITION]) != 2:
            msg = '"' + const.POSITION + '" has only 2 integer.'
            raise ConfigurationError(msg)
        config.position = tuple(args[const.POSITION])
    
    # SIZEの型チェック
    if const.SIZE in args:
        if not type(args[const.SIZE]) is tuple:
            msg = '"' + const.SIZE + '" is not tuple.'
            raise ConfigurationError(msg)
        elif len(args[const.SIZE]) != 2:
            msg = '"' + const.SIZE + '" has only 2 integer.'
            raise ConfigurationError(msg)
        config.size = tuple(args[const.SIZE])
    
    config.is_initialized = True

def run(host = 'localhost', port = 0):
    """
    morayライブラリを実行
    
    Attributes:
        host (str): サーバのホスト
        port (int): サーバのポート番号
    
    """
    
    # 設定が初期化済みかチェック
    if not config.is_initialized:
        msg = '"moray" is not initialized. Call "moray.init(root)".'
        raise ConfigurationError(msg)
    
    # HOSTチェック
    if host is None or host == 'localhost':
        config.host = 'localhost'
    elif re.match(r'\d+\.\d+\.\d+\.\d+', host) is None:
        msg = '"' + const.HOST + '" is not "localhost" or "xxx.xxx.xxx.xxx".'
        raise ConfigurationError(msg)
    else:
        for num in host.split('.'):
            if int(num) < 0 or 255 < int(num):
                msg = '"' + const.HOST + '" is not "localhost" or "xxx.xxx.xxx.xxx".'
                raise ConfigurationError(msg)
        config.host = host
    
    # PORTチェック
    if port < 0 or 65535 < port:
        msg = '"' + const.PORT + '" is less than 0 or greater than 65535.'
        raise ConfigurationError(msg)
    config.port = port
    
    _execute_moray()

def expose(func):
    """
    デコレータ
    JavaScriptから呼び出すファンクションを登録
    
    Attributes:
        func (function): 登録するファンクション
    
    """
    
    _register(func.__module__, func.__name__, func)
    
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    
    return wrapper

# ===== 以下は別モジュールに実装する =====
def _execute_moray():
    print('_execute_moray')

def _register(module, name, func):
    print('_register')
    print('  module: ' + module)
    print('  name: ' + name)
