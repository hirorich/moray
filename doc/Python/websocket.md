# WebSocket
- クライアントとサーバの双方向通信を可能にする、単一のTCPコネクション上のプロトコル

***
## 目次
- [ざっくりとした仕組み](#ざっくりとした仕組み)
- [サンプルコード](#サンプルコード)
  - [サーバ（Python、Bottle）](#サーバPythonBottle)
  - [クライアント（JavaScript）](#クライアントJavaScript)
- [参考](#参考)

***
## ざっくりとした仕組み
HTTPのUpgradeヘッダを使用し、プロトコルの変更を行うことでWebSocketによる通信の確立を行う
- この通信の確立をopeningハンドシェク（または単にハンドシェイク）という

ハンドシェイクが終わると、TCP上で双方向通信が可能になる
- フレームという単位でデータを送受信する
- HTTPと比べるとデータが少ない
  - メインデータ以外はWebSocketでは最大14byteほどらしい
  - HTTPはリクエストヘッダーだけで数百byteあるらしい

***
## サンプルコード
### サーバ（Python、Bottle）
``` python
import bottle
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

app = bottle.Bottle()

@app.route('/')
def main():
    return bottle.static_file('index.html', root='./')

@app.route('/websocket', apply=[websocket])
def echo(ws):
    while True:
        msg = ws.receive()
        if msg is not None:
            ws.send('echo:{0}'.format(msg))
        else:
            break

app.run(
    host = 'localhost',
    port = 8080,
    server = GeventWebSocketServer
)
```
- WebSocketで受け取る変数 ws は [geventwebsocket.websocket.WebSocket](https://github.com/jgelens/gevent-websocket/blob/master/geventwebsocket/websocket.py#L17) 型
  - receive
    - 送られたメッセージを受信
  - send
    - メッセージを送信

### クライアント（JavaScript）
``` javascript
// WebSocket 接続を開く
const socket = new WebSocket('ws://localhost:8080/websocket');

// 接続が開いたときのイベントリスナー
socket.onopen = function (event) {
    console.log('WebSocket opened');
}

// 接続が閉じたときのイベントリスナー
socket.onclose = function (event) {
    console.log('WebSocket closed');
}

// エラー時のイベントリスナー
socket.onerror = function (event) {
    console.log('WebSocket error: ', event);
}

// メッセージの待ち受けイベントリスナー
socket.onmessage = function (message_event) {
    console.log('Message from server ', message_event.data);
}

// メッセージ送信
socket.send('Message from client');

// WebSocket 接続を閉じる
socket.close();
```

***
## 参考
- [今さら聞けないWebSocket~WebSocketとは~](https://qiita.com/chihiro/items/9d280704c6eff8603389)
- [WebSocketについて調べてみた。](https://qiita.com/south37/items/6f92d4268fe676347160)
- [WebSocket](https://developer.mozilla.org/ja/docs/Web/API/WebSocket)
- [BottleフレームワークでWebsocket通信を行う](https://symfoware.blog.fc2.com/blog-entry-2426.html)
