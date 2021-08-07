"""
Flaskサンプル
http://localhost:3500/

"""

import bottle
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

app = bottle.Bottle()

@app.route('/')
def index():
    return bottle.static_file('index.html', root='./test_pkg/bottle_static')

@app.route('/<file_path>')
def file_path(file_path):
    return bottle.static_file(file_path, root='./test_pkg/bottle_static')

@app.route('/websocket', apply=[websocket])
def bottle_websocket(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send('echo:' + msg)
        else:
            break

app.run(
    host='localhost',
    port=8080,
    reloader=True,
    debug=True,
    server=GeventWebSocketServer
)

