"""
サーバ起動とブラウザ起動を制御

"""

import requests, socket
from threading import Thread

from moray import _browser, _config, _server

def run():
    """
    スレッドを分ける
    メインスレッド: 内部サーバ起動
    デーモンスレッド: 起動確認 -> ブラウザ起動
    """
    
    # ポート番号生成
    generate_port()
    
    # 初期表示URL生成
    url = generate_start_url()
    
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

def generate_port():
    """
    ポート番号を生成
    """
    
    port = _config.port
    if port == 0:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(('localhost', 0))
            port = sock.getsockname()[1]
    
    _config.generated_port = port

def generate_start_url():
    """
    初期表示URLを生成
    """
    
    return 'http://localhost:{0}/{1}'.format(_config.generated_port, _config.start_page)

def run_server():
    """
    内部サーバ起動
    """
    
    _server.run(_config.generated_port)

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

