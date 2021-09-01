"""
morayが提供するAPIのInterface
"""

from moray import _browser, _checker, _config, _runner, _server
from moray._browser import chrome
from moray._module import py
from moray.exception import MorayRuntimeError, SupportError

_ROOT = 'root'
_START_PAGE = 'start_page'
_BROWSER = 'browser'
_CMDLINE_ARGS = 'cmdline_args'
_POSITION = 'position'
_SIZE = 'size'
_HOST = 'host'
_PORT = 'port'

class _CLASS():
    pass
js = _CLASS()

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
    
    # root入力チェック
    _checker.check_not_None(root, _ROOT)
    _checker.check_str(root, _ROOT)
    _checker.check_not_whitespace(root, _ROOT)
    root = root.strip(' ')
    _checker.check_exist(root)
    
    # start_page入力チェック
    _checker.check_not_None(start_page, _START_PAGE)
    _checker.check_str(start_page, _START_PAGE)
    start_page = start_page.strip(' ')
    
    # host入力チェック
    _checker.check_not_None(host, _HOST)
    _checker.check_str(host, _HOST)
    _checker.check_not_whitespace(host, _HOST)
    host = host.strip(' ')
    _checker.check_host(host, _HOST)
    
    # port入力チェック
    _checker.check_not_None(port, _PORT)
    _checker.check_int(port, _PORT)
    _checker.check_port(port, _PORT)
    port = _server.generate_port(port)
    
    # browser入力チェック
    _checker.check_not_None(browser, _BROWSER)
    _checker.check_str(browser, _BROWSER)
    browser = browser.strip(' ')
    if not _browser.is_supported(browser):
        msg = '"{0}" is not a supported browser.'.format(browser)
        raise SupportError(msg)
    
    # cmdline_args入力チェック
    _checker.check_not_None(cmdline_args, _CMDLINE_ARGS)
    _checker.check_list_or_tuple(cmdline_args, _CMDLINE_ARGS)
    cmdline_args = list(cmdline_args)
    
    # position入力チェック
    if position is not None:
        _checker.check_list_or_tuple(position, _POSITION)
        _checker.check_2_int_list_or_tuple(position, _POSITION)
        position = tuple(position)
    
    # size入力チェック
    if size is not None:
        _checker.check_list_or_tuple(size, _SIZE)
        _checker.check_2_int_list_or_tuple(size, _SIZE)
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

def expose(func):
    """
    デコレータ
    JavaScriptから呼び出せるようファンクションを公開
    
    Attributes:
        func (function): 登録するファンクション
    """
    
    if callable(func):
        py.register(func)
    else:
        raise MorayRuntimeError('"moray.expose" can only be used for "function".')
    
    return func
