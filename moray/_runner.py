"""
サーバ起動とブラウザ起動を制御

"""

import requests
from threading import Thread

from moray import _browser, _config, _server

def run():
    """
    スレッドを分ける
    メインスレッド: 内部サーバ起動
    デーモンスレッド: 起動確認 -> ブラウザ起動
    """
    
    # ブラウザ起動(別スレッド)
    deamon_t = Thread(target=open_browser)
    deamon_t.setDaemon(True)
    deamon_t.start()
    
    # サーバ起動
    _server.run()

def open_browser():
    """
    requestsによるGETでサーバーが起動しているか確認
    アプリモードでブラウザ表示
    """
    
    # サーバ起動確認
    connect_timeout = 3.0
    read_timeout = 5.0
    try:
        res = requests.get(
            _server.generate_confirm_running_url(),
            timeout = (connect_timeout, read_timeout)
        )
        if not res.ok:
            raise RuntimeError('Could not confirm server run.')
    except Exception as e:
        # requests.exceptions.Timeout など
        raise
    
    # 初期表示URL生成
    url = _server.generate_start_url()
    
    # 初期ページ表示
    if _config.develop_mode:
        print('This is develop mode. Open your browser.')
        print('  URL: {0}'.format(url))
    else:
        _browser.open(_config.browser, url, _config.cmdline_args)
