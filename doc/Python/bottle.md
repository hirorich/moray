# Bottle
- Python用のWSGIマイクロWebフレームワーク
- 本ドキュメントでは使用している機能についてのみ記載

***
## 目次
- [ざっくりとした概要](#ざっくりとした概要)
- [サンプルコード](#サンプルコード)
- [API仕様](#api仕様)
  - [Bottle](#bottle-1)
    - [route](#route)
    - [run](#run)
  - [static_file](#staticfile)
- [参考](#参考)

***
## ざっくりとした概要
- Python用のWSGIマイクロWebフレームワーク
  - WSGI: Web Server Gateway Interface
    - WebサーバとWebアプリケーションを接続するための標準化されたインタフェース定義
- 単一のファイルモジュールで、Pythonの標準ライブラリ以外の依存関係はなし
- 高速・シンプル・軽量になるように設計されている
- 学習用、または小規模なアプリケーション作成に適している

***
## サンプルコード
``` python
import bottle

app = bottle.Bottle()

@app.route('/')
@app.route('/<path>')
def index(path = 'index.html'):
    return bottle.static_file(path, root = 'web')

app.run(host = 'locahost', port = 8080)
```

***
## API仕様
### [Bottle](https://bottlepy.org/docs/dev/api.html#bottle.Bottle)
- 各Bottleオブジェクトは1つの独立したWebアプリケーションを表す
- インスタンスは呼び出し可能なWSGIアプリケーション
- ルート、コールバック、プラグイン、リソース、設定で構成されている

### [route](https://bottlepy.org/docs/dev/api.html#bottle.Bottle.route)
- route(path=None, method='GET', callback=None, name=None, apply=None, skip=None, **config)
- 関数をリクエストURLにバインドするデコレーター
- <>で囲った部分はワイルドカード
- 詳細は以下参照
  - [Request Routing](https://bottlepy.org/docs/dev/routing.html?highlight=routing)

### [run](https://bottlepy.org/docs/dev/api.html#bottle.run)
- run(app=None, server='wsgiref', host='127.0.0.1', port=8080, interval=1, reloader=False, quiet=False, plugins=None, debug=None, config=None, **kargs)
- サーバーインスタンスを起動
- サーバーが終了するまでブロックする

### [static_file](https://bottlepy.org/docs/dev/tutorial.html#routing-static-files)
- 画像やCSSファイルなどの静的ファイルを提供する
- 返却値は [bottle.HTTPResponse](https://bottlepy.org/docs/dev/api.html#bottle.HTTPResponse) 型
- path
  - 対象のルートディレクトリからのパスを指定
- root
  - 検索対象のルートディレクトリを指定

***
## 参考
- [bottleドキュメント](https://bottlepy.org/docs/dev/tutorial.html)
- [bottleドキュメント(和訳版)](https://bottl-translate-ja.readthedocs.io/en/latest/01_1_tutorial.html)
- [Web Server Gateway Interface](https://ja.wikipedia.org/wiki/Web_Server_Gateway_Interface)
- [PythonのフレームワークBottleの活用方法【初心者向け】](https://techacademy.jp/magazine/19069)
- [Python Bottleフレームワークのサンプル](https://itsakura.com/python-bottle)
