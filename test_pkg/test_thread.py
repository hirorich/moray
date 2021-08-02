"""
Flaskサンプル
http://localhost:3500/

"""

import requests
from threading import Thread

from my_package import browser
from test_pkg import test_flask
app = test_flask.app

HOST='localhost'
PORT=3500

@app.route('/my_package/')
@app.route('/my_package/<name>')
def check(name=None):
    return 'Success'

def run():
    """
    Flask起動
    """
    
    app.run(host=HOST, port=PORT)

def daemon_thread():
    """
    requestsによるGETでサーバーが起動しているか確認
    """
    
    url = r'http://' + HOST + ':' + str(PORT) + '/'
    check_url = url + 'my_package/'
    connect_timeout = 3.0
    read_timeout = 5.0
    
    # 確認が取れるまで接続
    while True:
        try:
            res = requests.get(check_url, timeout=(connect_timeout, read_timeout))
            if res.ok:
                print('Success: ' + check_url)
                break
            else:
                print('Error: ' + check_url)
        except Exception as e:
            print('Exception: ' + check_url)
    
    open(url)
    print('daemon_thread STOP')

def open(url):
    """
    アプリモードで開く
    """
    
    browser_name = 'chrome'
    cmdline_args = ['--incognito']
    browser.open(browser_name, url, cmdline_args)

def test():
    main_t = Thread(target=run)
    deamon_t = Thread(target=daemon_thread)
    deamon_t.setDaemon(True)
    main_t.start()
    deamon_t.start()
