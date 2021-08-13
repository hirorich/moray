"""
アプリモードで対象ページを開く

"""

import subprocess

from moray._browser import chrome
from moray.exception import SupportError

CHROME = chrome.name

_browser_modules = {CHROME: chrome}

def is_supported(browser):
    """
    指定したブラウザがサポート対象かチェック
    
    Attributes:
        browser (str): チェック対象ブラウザ
    
    Returns:
        bool: ブラウザのサポート有無
    """
    
    return browser in _browser_modules

def open(browser, url, cmdline_args):
    """
    指定したブラウザで対象ページを開く
    
    Attributes:
        browser (str): 起動するブラウザ
        url (str): 接続先のURL
        cmdline_args (list<str>): コマンドライン引数
    """
    
    # 使用するブラウザモジュールを指定
    if is_supported(browser):
        browser_module = _browser_modules[browser]
    else:
        
        # 対象外ブラウザの場合
        # browser はサポート対象外のブラウザです。
        error_msg = '"{0}" is not a supported browser.'.format(browser)
        raise SupportError(error_msg)
    
    # 対象ページを開く
    path = browser_module.find_path()
    cmd = browser_module.create_command(path, url, cmdline_args)
    subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        creationflags=subprocess.CREATE_NO_WINDOW
    )
