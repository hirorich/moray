"""
morayで起動する内部サーバ設定
http://localhost:port/

ToDo:
    jsモジュール自動生成pyモジュール作成・呼び出し
"""

import bottle, json, socket
from bottle import HTTPResponse
from bottle.ext.websocket import GeventWebSocketServer, websocket

from moray import _config

app = bottle.Bottle()

@app.route('/moray/confirm_running')
def run_check():
    """
    サーバ起動確認用
    
    Returns:
        固定メッセージページ
    """
    
    return 'Success'

@app.route('/moray/py/<py_module>')
def py_module_script(py_module):
    """
    JavaScriptからPythonを呼び出すためのjsモジュールを生成
    生成したモジュールを返却
    
    Returns:
        JavaScriptからPythonを呼び出すためのjsモジュール
    """
    
    return bottle.static_file('{0}.js'.format(py_module), root='web/js/py')

@app.route('/moray/js/<core_module>')
def core_module_script(core_module):
    """
    生成したjsモジュール内で呼び出されるjsモジュールを生成
    生成したモジュールを返却
    
    Returns:
        生成したjsモジュール内で呼び出されるjsモジュール
    """
    
    return bottle.static_file('{0}.js'.format(core_module), root='web/js/core')

@app.route('/moray/ws', apply=[websocket])
def bottle_websocket(ws):
    """
    WebSocketの受け取り口
    
    Returns:
        pyモジュールの実行結果
    """
    
    while True:
        msg = ws.receive()
        if msg is None:
            break
        
        print(msg)
        parsed_msg = json.loads(msg)
        if parsed_msg['return']:
            print('return')
        else:
            print('call')
        
        ws.send(json.dumps(parsed_msg))

@app.route('/')
@app.route('/<path:path>')
def page(path = 'index.html'):
    """
    root配下のファイルを返却
        .html, .js, .css など
    
    Returns:
        root配下のページ
    """
    
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
