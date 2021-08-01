"""
Flaskサンプル
http://localhost:3500/

"""

import requests
from threading import Thread

from flask import Flask, render_template
app = Flask(__name__)

HOST='localhost'
PORT=3500

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

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
    connect_timeout = 3.0
    read_timeout = 5.0
    
    # 確認が取れるまで接続
    while True:
        try:
            res = requests.get(url, timeout=(connect_timeout, read_timeout))
            if res.ok:
                print('Success: ' + url)
                break
            else:
                print('Error: ' + url)
        except Exception as e:
            print('Exception: ' + url)
    
    print('daemon_thread STOP')

def test():
    main_t = Thread(target=run)
    deamon_t = Thread(target=daemon_thread)
    deamon_t.setDaemon(True)
    main_t.start()
    deamon_t.start()
