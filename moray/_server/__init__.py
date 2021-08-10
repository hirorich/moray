"""
morayで起動する内部サーバ
http://localhost:port/

"""

import bottle, json, socket
from bottle import HTTPResponse
from bottle.ext.websocket import GeventWebSocketServer, websocket

from moray import _config

app = bottle.Bottle()

@app.route('/moray/py/<py_module>')
def py_module_script(py_module):
    """
    JavaScriptからPythonを呼び出すためのjsモジュールを生成
    生成したモジュールを返却
    
    Return: JavaScriptからPythonを呼び出すためのjsモジュール
    """
    
    return bottle.static_file('{0}.js'.format(py_module), root='moray/js/py')

@app.route('/moray/core/<core_module>')
def core_module_script(core_module):
    """
    生成したjsモジュール内で呼び出されるjsモジュールを生成
    生成したモジュールを返却
    
    Return: 生成したjsモジュール内で呼び出されるjsモジュール
    """
    
    return bottle.static_file('{0}.js'.format(core_module), root='moray/js/core')

@app.route('/moray/ws', apply=[websocket])
def bottle_websocket(ws):
    """
    WebSocketの受け取り口
    
    Return: pyモジュールの実行結果
    """
    
    while True:
        msg = ws.receive()
        if msg is None:
            break
        
        print(msg)
        parsed_msg = json.loads(msg)
        return_msg = {'id': parsed_msg['id'], 'data': msg}
        ws.send(json.dumps(return_msg))

@app.route('/')
@app.route('/<path:path>')
def page(path = 'index.html'):
    """
    root配下のファイルを返却
        .html, .js, .css など
    
    Return: root配下のファイル
    """
    
    return bottle.static_file(path, root=_config.root)

def run():
    """
    サーバ起動
    
    Attributes:
        port (int): ポート番号
    """
    
    app.run(
        host = _config.host,
        port = _config.port,
        reloader = _config.develop_mode,
        debug = _config.develop_mode,
        server = GeventWebSocketServer
    )

def generate_port(port):
    """
    ポート番号を生成
    """
    
    if port == 0:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(('localhost', 0))
            port = sock.getsockname()[1]
    
    return port

def generate_start_url():
    """
    初期表示URLを生成
    """
    
    return 'http://localhost:{0}/{1}'.format(_config.port, _config.start_page)
