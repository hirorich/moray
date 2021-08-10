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
    
    # 初期表示URL生成
    url = _server.generate_start_url()
    
    # ブラウザ起動(別スレッド)
    if _config.develop_mode:
        print('This is develop mode. Open your browser.')
        print('  URL: {0}'.format(url))
    else:
        deamon_t = Thread(target=open_browser, args=(url,))
        deamon_t.setDaemon(True)
        deamon_t.start()
    
    # サーバ起動
    run_server()

def run_server():
    """
    内部サーバ起動
    """
    
    _server.run()

def open_browser(url):
    """
    requestsによるGETでサーバーが起動しているか確認
    アプリモードでブラウザ表示
    """
    
    # 確認が取れるまで接続
    connect_timeout = 3.0
    read_timeout = 5.0
    while True:
        try:
            res = requests.get(url, timeout=(connect_timeout, read_timeout))
            if res.ok:
                print('Success: {0}'.format(url))
                break
            else:
                print('Error: {0}'.format(url))
        except Exception as e:
            raise e
    
    # 初期ページ表示
    _browser.open(_config.browser, url, _config.cmdline_args)

