"""
Flaskサンプル
http://localhost:3500/

"""

import bottle, json
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
            print(msg)
            msg_data = json.loads(msg)
            print('  id: ' + msg_data['id'])
            print('  module: ' + msg_data['module'])
            print('  func: ' + msg_data['func'])
            re_obj = {'id': msg_data['id'], 'data': msg}
            re_msg = json.dumps(re_obj)
            print(re_msg)
            ws.send(re_msg)
        else:
            break

app.run(
    host='localhost',
    port=8080,
    reloader=True,
    debug=True,
    server=GeventWebSocketServer
)

