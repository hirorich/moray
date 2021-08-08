"""
morayで起動する内部サーバ
http://localhost:port/

"""

from moray import config
import bottle, json
from bottle import HTTPResponse
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

app = bottle.Bottle()

@app.route('/moray/py/<py_module>')
def py_module_script(py_module):
    """
    JavaScriptからPythonを呼び出すためのjsモジュールを生成
    生成したモジュールを返却
    
    Return: JavaScriptからPythonを呼び出すためのjsモジュール
    
    """
    
    return bottle.static_file(py_module + '.js', root='moray/js/py')

@app.route('/moray/core/<core_module>')
def core_module_script(core_module):
    """
    生成したjsモジュール内で呼び出されるjsモジュールを生成
    生成したモジュールを返却
    
    Return: 生成したjsモジュール内で呼び出されるjsモジュール
    
    """
    
    return bottle.static_file(core_module + '.js', root='moray/js/core')

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
def page(path = config.start_page):
    """
    root配下のファイルを返却
        .html, .js, .css など
    
    Return: root配下のファイル
    
    """
    
    return bottle.static_file(path, root=config.root)

def run(port):
    """
    サーバ起動
    
    Attributes:
        port (int): ポート番号
    
    """
    
    app.run(
        host=config.host,
        port=port,
        reloader=True,
        debug=True,
        server=GeventWebSocketServer
    )

