"""
サーバ起動とブラウザ起動を制御

"""

from moray import browser, config, server
import requests, socket
from threading import Thread

def run():
    """
    スレッドを分ける
    メインスレッド: 内部サーバ起動
    デーモンスレッド: 起動確認 -> ブラウザ起動
    
    """
    
    # ポート番号生成
    generate_port()
    
    # サーバとブラウザ起動
    deamon_t = Thread(target=daemon_thread)
    deamon_t.setDaemon(True)
    deamon_t.start()
    run_server()

def generate_port():
    """
    ポート番号を生成
    
    """
    
    port = config.port
    if port == 0:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(('localhost', 0))
            port = sock.getsockname()[1]
    
    config.generated_port = port

def run_server():
    """
    内部サーバ起動
    
    """
    
    server.run(config.generated_port)

def daemon_thread():
    """
    requestsによるGETでサーバーが起動しているか確認
    """
    
    url = r'http://' + config.host + ':' + str(config.generated_port) + '/'
    
    # 確認が取れるまで接続
    connect_timeout = 3.0
    read_timeout = 5.0
    while True:
        try:
            res = requests.get(url, timeout=(connect_timeout, read_timeout))
            if res.ok:
                print('Success: ' + url)
                break
            else:
                print('Error: ' + url)
        except Exception as e:
            raise e
    
    # 初期ページ表示
    browser.open(config.browser, url, config.cmdline_args)

