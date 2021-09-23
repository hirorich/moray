# moray
- eelを参考にしたJavaScriptによるGUI作成ライブラリ
- Python関数をモジュール単位で管理する

***
## 目次
- [経緯](#経緯)
- [開発環境構築](#開発環境構築)
- [使用ライブラリ一覧](#使用ライブラリ一覧)
- [使用方法](#使用方法)
  - [JavaScriptからPython関数呼び出し](#javascriptからpython関数呼び出し)
  - [PythonからJavaScript関数呼び出し](#pythonからjavascript関数呼び出し)
  - [moray起動](#moray起動)
  - [終了検知](#終了検知)
- [参考](#参考)

***
## 経緯
- PythonによるGUI作成のライブラリのうち、eelがJavaScriptでGUIを作成できるため愛用していた
- しかし、eelによるPythonの関数管理は関数名により行われるため、名前かぶりがないように管理するのが面倒
- よって、モジュールも含めて管理することで名前被りを防ぐよう対応する

***
## 開発環境構築
### Python
- python v.3.9
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

***
## 使用ライブラリ一覧
### Python
- [bottle](https://pypi.org/project/bottle/)
  - MIT License
  - 軽量Webフレームワーク
  - 以下を実行することでインストール
    ``` bash
    pip install bottle
    ```
- [bottle-websocket](https://pypi.org/project/bottle-websocket/)
  - MIT License
  - bottleでWebSocketを使用するためのプラグイン
  - 以下を実行することでインストール
    ``` bash
    pip install bottle-websocket
    ```
- [gevent](https://pypi.org/project/gevent/)
  - MIT License
  - bottle-websocketの依存ライブラリ
  - bottle-websocketインストール時にインストール
- [gevent-websocket](https://pypi.org/project/gevent-websocket/)
  - [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
  - bottle-websocketの依存ライブラリ
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
## 使用方法
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

### moray起動

### 終了検知

***
## 参考
- [eel](https://github.com/ChrisKnott/Eel)

