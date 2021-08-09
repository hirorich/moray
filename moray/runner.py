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
    
    # 初期表示URL生成
    url = generate_start_url()
    
    # ブラウザ起動(別スレッド)
    if config.develop_mode:
        print('This is develop mode. Open your browser.')
        print(f'  URL: {url}')
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
    
    port = config.port
    if port == 0:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(('localhost', 0))
            port = sock.getsockname()[1]
    
    config.generated_port = port

def generate_start_url():
    """
    初期表示URLを生成
    
    """
    
    return f'http://{config.host}:{str(config.generated_port)}/{config.start_page}'

def run_server():
    """
    内部サーバ起動
    
    """
    
    server.run(config.generated_port)

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
                print('Success: ' + url)
                break
            else:
                print('Error: ' + url)
        except Exception as e:
            raise e
    
    # 初期ページ表示
    browser.open(config.browser, url, config.cmdline_args)

