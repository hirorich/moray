"""
Flaskサンプル
http://localhost:3500/

"""

import bottle, json
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

app = bottle.Bottle()

@app.route('/moray/py/<py_module>')
def py_module(py_module):
    print('  /moray/py/<py_module>')
    print('  ' + py_module)
    return bottle.static_file(py_module + '.js', root='./test_pkg/moray/py')

@app.route('/moray/core/<core_module>')
def moray_core(core_module):
    print('  /moray/core/<core_module>')
    print('  ' + core_module)
    return bottle.static_file(core_module + '.js', root='./test_pkg/moray/core')

@app.route('/moray/ws', apply=[websocket])
def bottle_websocket(ws):
    print(ws)
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

@app.route('/')
def index():
    print('/')
    return bottle.static_file('index.html', root='./test_pkg/bottle_static')

@app.route('/<path:path>')
def file_path(path):
    print('  /<path:path>')
    print('  path: ' + path)
    return bottle.static_file(path, root='./test_pkg/bottle_static')

app.run(
    host='localhost',
    port=8080,
    reloader=True,
    debug=True,
    server=GeventWebSocketServer
)

