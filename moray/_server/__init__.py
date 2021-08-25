"""
morayで起動する内部サーバ設定
http://localhost:port/

ToDo:
    jsモジュール自動生成pyモジュール作成・呼び出し
"""

import bottle, json, pkg_resources, socket
from bottle import HTTPResponse
from bottle.ext.websocket import GeventWebSocketServer, websocket

from moray import _config
from moray._module import py

_RETURN = 'return'
_CALL = 'call'
_EXPOSE = 'expose'

root_module_js = pkg_resources.resource_filename('moray', r'_module\js')

app = bottle.Bottle()

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
    
    Returns:
        pyモジュールの実行結果
    """
    
    while True:
        msg = ws.receive()
        if msg is None:
            break
        
        print(msg)
        parsed_msg = json.loads(msg)
        method = parsed_msg['method']
        
        if method == _CALL:
            print(_CALL)
            id = parsed_msg['id']
            module = parsed_msg['module']
            func_name = parsed_msg['func_name']
            args = parsed_msg['args']
            
            result, is_success = _call_py_func(module, func_name, args)
            
            return_msg = {}
            return_msg['id'] = id
            return_msg['return'] = True
            return_msg['result'] = result
            return_msg['is_success'] = is_success
            
            ws.send(json.dumps(return_msg))
            
        elif method == _RETURN:
            print(_RETURN)
            id = parsed_msg['id']
            result = parsed_msg['result']
            is_success = parsed_msg['is_success']
            
        elif method == _EXPOSE:
            print(_EXPOSE)
            func_name = parsed_msg['func_name']
            print(func_name)

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

def _call_py_func(module, func_name, args):
    """
    exposeしたファンクションを呼び出す
    
    Attributes:
        module (str): 呼び出すモジュール名
        func_name (str): 呼び出すファンクション名
        args (dict): 引数
    
    Returns:
        ファンクションの実行結果
        実行成否(True:成功, False:失敗)
    """
    
    try:
        result = py.call(module, func_name, args)
        return result, True
    except:
        # ToDo: ログ出力
        result = 'calling python function is faild.'
        return result, False

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
