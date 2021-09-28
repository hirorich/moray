# moray
- PythonモジュールとJavaScriptを使ってHTML GUIを作成するパッケージ。
- Pythonの関数をモジュールで管理する。

***
## 目次
- [インストール](#インストール)
- [ディレクトリ構造](#ディレクトリ構造)
- [使用方法](#使用方法)
  - [アプリ起動](#アプリ起動)
  - [起動オプション](#起動オプション)
  - [JavaScriptからPython関数呼び出し](#javascriptからpython関数呼び出し)
  - [PythonからJavaScript関数呼び出し](#pythonからjavascript関数呼び出し)
  - [終了検知](#終了検知)
  - [ログ取得](#ログ取得)
- [使用パッケージ一覧](#使用パッケージ一覧)

***
## インストール
- 以下コマンドを実行。
  ```
  pip install moray
  ```

***
## ディレクトリ構造
- moray のアプリケーションは、.html, .js, .css などのフロントエンドと、Pythonスクリプトによるバックエンドで構成される。
- **/moray.js および /moray/ 配下は moray 内部で使用するため使用不可**
  ```
  python_script.py     <-- Pythonスクリプト
  web/                 <-- 静的ウェブディレクトリ
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
    - http://<span>localhost:動的に割り当てられたポート番号</span>/index.html が表示される

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
- **Python関数の呼び出しごとに別スレッド上で動作する**
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
## 使用パッケージ一覧
- [bottle-websocket](https://pypi.org/project/bottle-websocket/)
  - [MIT License](https://github.com/zeekay/bottle-websocket/blob/master/LICENSE)
- [requests](https://pypi.org/project/requests/)
  - [Apache License 2.0](https://github.com/psf/requests/blob/main/LICENSE)
- [Jinja2](https://pypi.org/project/Jinja2/)
  - [BSD License (BSD-3-Clause)](https://github.com/pallets/jinja/blob/main/LICENSE.rst)
