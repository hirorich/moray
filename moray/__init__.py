"""
morayが提供するAPIのInterface

"""

import re
from pathlib import Path

from moray import _browser, _config, _runner, _server
from moray._browser import chrome
from moray.exception import ConfigurationError, SupportError

_ROOT = 'root'
_START_PAGE = 'start_page'
_BROWSER = 'browser'
_CMDLINE_ARGS = 'cmdline_args'
_POSITION = 'position'
_SIZE = 'size'
_HOST = 'host'
_PORT = 'port'

def run(
        root,
        start_page = '',
        host = 'localhost',
        port = 0,
        browser = chrome.name,
        cmdline_args = [],
        position = None,
        size = None
    ):
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
    
    """
    
    # root入力チェック
    _check_not_None(root, _ROOT)
    _check_str(root, _ROOT)
    _check_not_whitespace(root, _ROOT)
    root = root.strip(' ')
    _check_exist(root)
    
    # start_page入力チェック
    _check_not_None(start_page, _START_PAGE)
    _check_str(start_page, _START_PAGE)
    start_page = start_page.strip(' ')
    
    # host入力チェック
    _check_not_None(host, _HOST)
    _check_str(host, _HOST)
    _check_not_whitespace(host, _HOST)
    host = host.strip(' ')
    _check_host(host)
    
    # port入力チェック
    _check_not_None(port, _PORT)
    _check_int(port, _PORT)
    _check_port(port)
    port = _server.generate_port(port)
    
    # browser入力チェック
    _check_not_None(browser, _BROWSER)
    _check_str(browser, _BROWSER)
    browser = browser.strip(' ')
    if not _browser.is_supported(browser):
        msg = '"{0}" is not a supported browser.'.format(browser)
        raise SupportError(msg)
    
    # cmdline_args入力チェック
    _check_not_None(cmdline_args, _CMDLINE_ARGS)
    _check_list_or_tuple(cmdline_args, _CMDLINE_ARGS)
    cmdline_args = list(cmdline_args)
    
    # position入力チェック
    if position is not None:
        _check_list_or_tuple(position, _POSITION)
        _check_2_int_list_or_tuple(position, _POSITION)
        position = tuple(position)
    
    # size入力チェック
    if size is not None:
        _check_list_or_tuple(size, _SIZE)
        _check_2_int_list_or_tuple(size, _SIZE)
        size = tuple(size)
    
    _config.root = root
    _config.start_page = start_page
    _config.host = host
    _config.port = port
    _config.browser = browser
    _config.cmdline_args = cmdline_args
    _config.position = position
    _config.size = size

    # サーバ起動・ブラウザ起動
    _runner.run()

def _check_not_None(value, name):
    """
    Noneチェック
    
    Attributes:
        value: チェック対象変数
        name (str): チェック対象項目名
    
    Raises:
        ConfigurationError: チェックエラー
    """
    
    if value is None:
        msg = '"{0}" is None.'.format(name)
        raise ConfigurationError(msg)

def _check_str(value, name):
    """
    strチェック
    
    Attributes:
        value: チェック対象変数
        name (str): チェック対象項目名
    
    Raises:
        ConfigurationError: チェックエラー
    """
    
    if type(value) is not str:
        msg = '"{0}" is not "str" type.'.format(name)
        raise ConfigurationError(msg)

def _check_int(value, name):
    """
    intチェック
    
    Attributes:
        value: チェック対象変数
        name (str): チェック対象項目名
    
    Raises:
        ConfigurationError: チェックエラー
    """
    
    if type(value) is not int:
        msg = '"{0}" is not "int" type.'.format(name)
        raise ConfigurationError(msg)

def _check_list_or_tuple(value, name):
    """
    list of tupleチェック
    
    Attributes:
        value: チェック対象変数
        name (str): チェック対象項目名
    
    Raises:
        ConfigurationError: チェックエラー
    """
    
    if type(value) is not list and type(value) is not tuple:
        msg = '"{0}" is not "list" or "tuple" type.'.format(name)
        raise ConfigurationError(msg)

def _check_not_whitespace(value, name):
    """
    空白はエラー
    
    Attributes:
        value (str): チェック対象変数
        name (str): チェック対象項目名
    
    Raises:
        ConfigurationError: チェックエラー
    """
    
    value = value.strip(' ')
    if value == '':
        msg = '"{0}" is whitespace.'.format(name)
        raise ConfigurationError(msg)

def _check_exist(value):
    """
    存在チェック
    
    Attributes:
        value (str): チェック対象変数
    
    Raises:
        ConfigurationError: チェックエラー
    """
    
    value = Path(value.strip(' '))
    if not value.exists():
        msg = '"{0}" is not exist.'.format(str(value))
        raise ConfigurationError(msg)

def _check_2_int_list_or_tuple(value, name):
    """
    list<int, int> or tuple<int, int>チェック
    
    Attributes:
        value (list or tuple): チェック対象変数
        name (str): チェック対象項目名
    
    Raises:
        ConfigurationError: チェックエラー
    """
    
    # 要素数チェック
    msg = '"{0}" has only 2 "int" type.'.format(name)
    if len(value) != 2:
        raise ConfigurationError(msg)
    
    # 要素内の型チェック
    for item in value:
        if type(item) is not int:
            raise ConfigurationError(msg)

def _check_host(host):
    """
    HOSTチェック
        localhost
        xxx.xxx.xxx.xxx(0 <= xxx <= 255)
    
    Attributes:
        host (str): サーバのホスト
    
    Raises:
        ConfigurationError: チェックエラー
    """
    
    msg = '"{0}" is not "localhost" or "xxx.xxx.xxx.xxx".(0 <= xxx <= 255)'.format(_HOST)
    if host == 'localhost':
        return
    elif re.match(r'\d+\.\d+\.\d+\.\d+', host) is None:
        raise ConfigurationError(msg)
    else:
        for num in host.split('.'):
            if int(num) < 0 or 255 < int(num):
                raise ConfigurationError(msg)

def _check_port(port):
    """
    PORTチェック
        0 <= port <= 65535)
    
    Attributes:
        port (int): サーバのポート番号
    
    Raises:
        ConfigurationError: チェックエラー
    """
    
    if port < 0 or 65535 < port:
        msg = '"{0}" is less than 0 or greater than 65535.'.format(_PORT)
        raise ConfigurationError(msg)

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
def _register(module, name, func):
    print('_register')
    print('  module: ' + module)
    print('  name: ' + name)
