"""
Flaskサンプル
http://localhost:3500/

"""

import requests
from threading import Thread

from moray import browser
from test_pkg import test_flask
from flask import render_template, Response
app = test_flask.app

HOST='localhost'
PORT=3500

@app.route('/jsSample.html')
def show_html():
    return render_template('jsSample.html')

@app.route('/moray.js')
def js_sample():
    res = Response('alert("moray.js");')
    res.content_type = 'text/javascript; charset=utf-8'
    return res

def run():
    """
    Flask起動
    """
    
    app.run(host=HOST, port=PORT)

def daemon_thread():
    """
    requestsによるGETでサーバーが起動しているか確認
    """
    
    check_url = r'http://' + HOST + ':' + str(PORT) + '/'
    url = check_url + 'jsSample.html'
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
