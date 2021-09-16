"""
morayで起動する内部サーバ設定
http://localhost:port/
"""

import bottle, pkg_resources, os, socket, time
from bottle import HTTPResponse
from bottle.ext.websocket import GeventWebSocketServer, websocket
from threading import Thread

from moray import _config, _module
from moray._module import py

root_module_js = pkg_resources.resource_filename('moray', r'_module\js')

app = bottle.Bottle()
_websockets=[]

@app.route('/moray/confirm_running')
def run_check():
    """
    サーバ起動確認用
    
    Returns:
        固定メッセージページ
    """
    
    return 'Success'

@app.route('/moray/py/<py_module>.js')
def py_module_script(py_module):
    """
    JavaScriptからPythonを呼び出すためのjsモジュールを生成
    生成したモジュールを返却
    
    Returns:
        JavaScriptからPythonを呼び出すためのjsモジュール
    """
    
    body = py.render(py_module)
    res = HTTPResponse(status=200, body=body)
    res.set_header('Content-type', 'text/javascript')
    return res

@app.route('/moray/js/<core_module>')
def core_module_script(core_module):
    """
    生成したjsモジュール内で呼び出されるjsモジュールを生成
    生成したモジュールを返却
    
    Returns:
        生成したjsモジュール内で呼び出されるjsモジュール
    """
    
    return bottle.static_file('{0}.js'.format(core_module), root=root_module_js)

@app.route('/moray.js')
def moray_script():
    """
    生成したjsモジュール内で呼び出されるjsモジュールを生成
    生成したモジュールを返却
    
    Returns:
        生成したjsモジュール内で呼び出されるjsモジュール
    """
    
    return bottle.static_file('moray.js', root=root_module_js)

@app.route('/moray/ws', apply=[websocket])
def bottle_websocket(ws):
    """
    WebSocketの受け取り口
    
    Attributes:
        ws (geventwebsocket.websocket.WebSocket): WebSocket接続オブジェクト
    """
    
    _websockets.append(ws)
    while True:
        msg = ws.receive()
        if msg is None:
            break
        
        # スレッドを分けて処理
        deamon_t = _module.WebsocketReact(ws, msg)
        deamon_t.setDaemon(True)
        deamon_t.start()
    
    # websocketが閉じられた際の処理
    deamon_t = Thread(target=_onclose_websocket, args=(ws,))
    deamon_t.setDaemon(True)
    deamon_t.start()

@app.route('/')
@app.route('/<path:path>')
def page(path = 'index.html'):
    """
    root配下のファイルを返却
        .html, .js, .css など
    
    Returns:
        root配下のページ
    """
    if path[-1] == '/':
        path += 'index.html'
    
    return bottle.static_file(path, root=_config.root)

def run():
    """
    サーバ起動
    """
    
    app.run(
        host = _config.host,
        port = _config.port,
        reloader = False,
        debug = False,
        server = GeventWebSocketServer
    )

def generate_port(port):
    """
    ポート番号を生成
    
    Returns:
        int: 生成したポート番号
    """
    
    if port == 0:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(('localhost', 0))
            port = sock.getsockname()[1]
    
    return port

def generate_start_url():
    """
    初期表示URLを生成
    
    Returns:
        str: 初期表示URL
    """
    
    return 'http://localhost:{0}/{1}'.format(_config.port, _config.start_page)

def generate_confirm_running_url():
    """
    サーバ起動確認用URLを生成
    
    Returns:
        str: サーバ起動確認用URL
    """
    
    return 'http://localhost:{0}/moray/confirm_running'.format(_config.port)

def _onclose_websocket(ws):
    """
    WebSocketが閉じられた際の処理
    
    Attributes:
        ws (geventwebsocket.websocket.WebSocket): WebSocket接続オブジェクト
    """
    
    # websocketに紐づくメモリを解放
    _module.unexpose(ws)
    _websockets.remove(ws)
    
    # 接続がない場合は終了
    if len(_websockets) == 0:
        time.sleep(3)
        if len(_websockets) == 0:
            print('exit.')
            os._exit(0)
