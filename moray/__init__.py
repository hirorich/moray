from moray import browser, chrome
from moray.exception import ConfigurationError, SupportError
from pathlib import Path

ROOT = 'root'
START_PAGE = 'start_page'
BROWSER = 'browser'
CMDLINE_ARGS = 'cmdline_args'
POSITION = 'position'
SIZE = 'size'
HOST = 'host'
PORT = 'port'

_default_moray_args = {
    ROOT: None,
    START_PAGE : None,
    BROWSER: chrome.name,
    CMDLINE_ARGS: ['--disable-http-cache', '--incognito'],
    POSITION: None,
    SIZE: None,
    HOST: 'localhost',
    PORT: 0
}

_moray_args = {}

def init(root, **kwargs):
    _moray_args.update(_default_moray_args)
    _moray_args.update(kwargs)
    
    # ROOTの初期値設定
    if root is None or root.strip(' ') == '':
        error_msg = '"' + ROOT + '" is unspecified or whitespace.'
        raise ConfigurationError(error_msg)
    root = root.strip(' ')
    
    # ROOTフォルダの存在チェック
    root_path = Path(root)
    if not root_path.exists():
        error_msg = '"' + str(root_path) + '" is not exist.'
        raise ConfigurationError(error_msg)
    _moray_args[ROOT] = root
    
    # START_PAGEの初期値設定
    start_page = _moray_args[START_PAGE]
    if start_page is None or start_page.strip(' ') == '':
        start_page = 'index.html'
    else:
        start_page = start_page.strip(' ')
    
    # ROOT/START_PAGEの存在チェック
    start_path = root_path.joinpath(start_page)
    if not start_path.exists():
        error_msg = '"' + str(start_path) + '" is not exist.'
        raise ConfigurationError(error_msg)
    _moray_args[START_PAGE] = start_page
    
    # ブラウザのサポートチェック
    if _moray_args[BROWSER] is None:
        error_msg = '"' + BROWSER + '" is unspecified.'
        raise ConfigurationError(error_msg)
    elif not browser.is_supported(_moray_args[BROWSER]):
        error_msg = '"' + _moray_args[BROWSER] + '" is not a supported browser.'
        raise SupportError(error_msg)
    
    # CMDLINE_ARGSの型チェック
    if not type(_moray_args[CMDLINE_ARGS]) is list:
        error_msg = '"' + CMDLINE_ARGS + '" is not list.'
        raise ConfigurationError(error_msg)
    
    # POSITIONの型チェック
    if _moray_args[POSITION] is None:
        pass
    elif type(_moray_args[POSITION]) is tuple:
        if len(_moray_args[POSITION]) != 2:
            error_msg = '"' + POSITION + '" has only 2 integer.'
            raise ConfigurationError(error_msg)
    else:
        error_msg = '"' + POSITION + '" is not tuple or None.'
        raise ConfigurationError(error_msg)
    
    # SIZEの型チェック
    if _moray_args[SIZE] is None:
        pass
    elif type(_moray_args[SIZE]) is tuple:
        if len(_moray_args[SIZE]) != 2:
            error_msg = '"' + SIZE + '" has only 2 integer.'
            raise ConfigurationError(error_msg)
    else:
        error_msg = '"' + SIZE + '" is not tuple or None.'
        raise ConfigurationError(error_msg)

def run(host = 'localhost', port = 0):
    if len(_moray_args) == 0:
        error_msg = '"moray" is not initialized. Call "moray.init(root)".'
        raise ConfigurationError(error_msg)
    
    # HOSTチェック
    if host != 'localhost':
        error_msg = '"' + _HOST + '" is only "localhost".'
        raise SupportError(error_msg)
    _moray_args[HOST] = host
    
    # PORTチェック
    _moray_args[PORT] = port
    
    _execute_moray(_moray_args)

def expose(func):
    
    _register(func.__module__, func.__name__, func)
    
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    
    return wrapper

# ===== 以下は別モジュールに実装する =====
def _execute_moray(moray_args):
    print('_execute_moray')
    print(moray_args)

def _register(module, name, func):
    print('_register')
    print('  module: ' + module)
    print('  name: ' + name)
