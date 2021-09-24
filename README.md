# moray
- eelを参考にしたJavaScriptによるGUI作成ライブラリ
- Python関数をモジュール単位で管理する

***
## 目次
- [経緯](#経緯)
- [使用Pyrhonライブラリ一覧](#使用pythonライブラリ一覧)
- [フォルダ構造](#フォルダ構造)
- [使用方法](#使用方法)
  - [アプリ起動](#アプリ起動)
  - [起動オプション](#起動オプション)
  - [JavaScriptからPython関数呼び出し](#javascriptからpython関数呼び出し)
  - [PythonからJavaScript関数呼び出し](#pythonからjavascript関数呼び出し)
  - [終了検知](#終了検知)
  - [ログ取得](#ログ取得)
- [開発環境構築](#開発環境構築)
- [参考](#参考)

***
## 経緯
- PythonによるGUI作成のライブラリのうち、eelがJavaScriptでGUIを作成できるため愛用していた
- しかし、eelによるPythonの関数管理は関数名により行われるため、名前かぶりがないように管理するのが面倒
- よって、モジュールも含めて管理することで名前被りを防ぐよう対応する

***
## 使用Pythonライブラリ一覧
各ライブラリの詳細は [使用ライブラリを個別にインストールする場合](#使用ライブラリを個別にインストールする場合) を確認
- [bottle-websocket](https://pypi.org/project/bottle-websocket/)
  - MIT License
- [bottle](https://pypi.org/project/bottle/)
  - MIT License
- [gevent-websocket](https://pypi.org/project/gevent-websocket/)
  - [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
- [gevent](https://pypi.org/project/gevent/)
  - MIT License
- [requests](https://pypi.org/project/requests/)
  - [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
- [Jinja2](https://pypi.org/project/Jinja2/)
  - BSD License (BSD-3-Clause)

***
## フォルダ構造
- moray のアプリケーションは、.html, .js, .css などのフロントエンドと、Pythonスクリプトによるバックエンドに分かれる
  ```
  python_script.py     <-- Pythonスクリプト
  web/                 <-- 静的ウェブフォルダ
    index.html
    css/
      style.css
    img/
      logo.png
  ```

***
## 使用方法
### アプリ起動
- 初期表示ページ index.html を含む全てのフロントエンドファイルを web ディレクトリに配置した場合、以下のように起動する
  ``` python
  import moray
  
  moray.run('web')
  ```
    - http://localhost:動的に割り当てられたポート番号/index.html が表示される

### 起動オプション
- moray.run() には、キーワード引数として以下の追加オプションを渡すことができる
  - start_page
    - str 型（デフォルト：''）
    - 初期表示するページ
      - '' の場合は index.html が表示される
  - host
    - str 型（デフォルト：'localhost'）
    - サーバのホスト
      - 'localhost' または IPアドレス の形式で指定可能
  - port
    - int 型（デフォルト：0）
    - サーバのポート番号
      -  0 または 1025以上65535以下の値 が指定可能
  - browser
    - str 型（デフォルト：'chrome'）
    - 使用するブラウザ
      - 'chrome' のみサポート
  - cmdline_args
    - list<str> 型（デフォルト：[]）
    - ブラウザの起動引数
      - chromeの場合以下引数が自動的に指定される
        - '--disable-http-cache' '--incognito'
  - position
    - tuple<int, int> 型（デフォルト：None）
    - ブラウザを開いた際の位置(x, y)
      - 位置を指定しない場合は None を指定する
  - size
    - tuple<int, int> 型（デフォルト：None）
    - ブラウザを開いた際のサイズ(x, y)
      - サイズを指定しない場合は None を指定する
- 使用例
  ``` python
  import moray
  
  moray.run(
      'web',
      start_page = 'index.html',
      host = 'localhost',
      port = 8000,
      browser = 'chrome',
      cmdline_args = [--disable-dev-tools],
      position = (400, 200),
      size = (800, 600)
  )
  ```

### JavaScriptからPython関数呼び出し
- 呼び出されたPython関数はメインスレッドでないため注意
- py_module.py
  ``` python
  import moray
  
  # jsから呼び出せるようデコレータにより登録
  @moray.expose
  def py_func(arg):
      return 'result'
  ```
- js_module.js
  ``` javascript
  // 登録されたPython関数読み込み
  // import {関数名} from '/moray/py/モジュール名.js'
  import {py_func} from '/moray/py/py_module.js'
  
  // 返却値を取得する場合
  // Promiseオブジェクトのthen, catchにより取得
  py_func('arg').then(
      // 正常終了時は実行結果が返却される
      v => ・・・
  ).catch(
      // 異常終了時は例外メッセージが返却される
      v => ・・・
  )

  // 実行結果の取得が不要な場合は 関数名(引数) で良い
  py_func('arg')
  ```

### PythonからJavaScript関数呼び出し
- 呼び出されたJavaScript関数内でさらにPython関数を呼び出した場合、呼び出し元のPython関数と別スレッドであるため注意
- js_module.js
  ``` javascript
  import moray from '/moray.js'
  import {py_func} from '/moray/py/py_module.js'
  
  // pythonから呼び出せるよう登録
  const js_func(arg) = function() {
      return 'result'
  }
  moray.expose(js_func)
  
  // Python関数呼び出し
  py_func()
  ```
- py_module.py
  ``` python
  import moray
  
  def other_func():
      # 実行結果の取得が不要な場合は moray.js.関数名(引数) で良い
      moray.js.js_func('arg')
  
  @moray.expose
  def py_func():
      
      try:
          # 実行結果は moray.js.関数名(引数)() で取得
          result = moray.js.js_func('arg')()
      except Exception as e:
          # 異常終了時は実行結果取得時に例外発生
          print(e)
      
      # 同一スレッド内であれば別関数からも呼び出し可能
      other_func()
  ```

### 終了検知
- 不測の事態によりmorayが終了してしまった場合 moray.onclose によって終了したことを検知可能
- js_module.js
  ``` javascript
  import moray from '/moray.js'
  
  // moray.onclose に関数を登録する
  // evt には null が渡される
  moray.onclose = function(evt) {
      alert('moray closed');
  }
  ```

### ログ取得
- moray 内では logging モジュールによるログ出力を行うため、 moray モジュールに対してロガーを設定することでロギング可能
- ロガー設定例
  ``` python
  import logging
  
  format = '[%(asctime)s][%(levelname)s] %(message)s (at %(name)s:%(lineno)s)'
  formatter = logging.Formatter(format)
  
  handler = logging.StreamHandler()
  handler.setLevel(logging.DEBUG)
  handler.setFormatter(formatter)
  
  logger = logging.getLogger('moray')
  logger.addHandler(handler)
  logger.setLevel(logging.INFO)
  ```

***
## 開発環境構築
### Python
- 環境作成
  ``` bash
  py -3.9 -m venv .venv
  ```
- 環境切り替え
  ``` bash
  .venv\Scripts\activate
  ```
- pip最新化
  ``` bash
  python -m pip install --upgrade pip
  ```
- 使用ライブラリを一括インストール
  ``` bash
  pip install -r requirements.txt
  ```

### 使用ライブラリを個別にインストールする場合
- [bottle-websocket](https://pypi.org/project/bottle-websocket/)
  - MIT License
  - bottleでWebSocketを使用するためのプラグイン
  - 以下を実行することでインストール
    ``` bash
    pip install bottle-websocket
    ```
- [bottle](https://pypi.org/project/bottle/)
  - MIT License
  - 軽量Webフレームワーク
  - bottle-websocketの依存ライブラリ
  - bottle-websocketインストール時にインストール
- [gevent-websocket](https://pypi.org/project/gevent-websocket/)
  - [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
  - bottle-websocketの依存ライブラリ
  - bottle-websocketインストール時にインストール
- [gevent](https://pypi.org/project/gevent/)
  - MIT License
  - gevent-websocketの依存ライブラリ
  - bottle-websocketインストール時にインストール
- [requests](https://pypi.org/project/requests/)
  - [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
  - サーバ起動確認に使用
  - 以下を実行することでインストール
    ``` bash
    pip install requests
    ```
- [Jinja2](https://pypi.org/project/Jinja2/)
  - BSD License (BSD-3-Clause)
  - テンプレートエンジン
  - 以下を実行することでインストール
    ``` bash
    pip install Jinja2
    ```

***
## 参考
- [eel](https://github.com/ChrisKnott/Eel)

