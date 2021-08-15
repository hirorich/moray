# moray
***
## moray とは
- eelを参考にしたGUI部品
- 関数をパッケージごとに管理
- 使用想定ライブラリ
  - Python
    - bottle 0.12
  - JavaScript
    - React 17
  - CSS
    - Bootstrap 5

***
## 経緯
- pythonによるGUI作成のライブラリのうち、eelがjavascriptでGUIを作成できるため愛用していた
- しかし、eelによるpythonの関数管理は関数名により行われるため、名前かぶりがないように管理するのが面倒
- よって、モジュールも含めて管理することで名前被りを防ぐよう対応したい
- またeel.jsも管理したpythonモジュールごとに分割し、javascriptモジュールとして読み込めるようにしたい

***
## 環境構築
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
## 使用ライブラリ
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

***
## 使用方法(想定)
### Javascript -> Python
- py_module.py
  ``` python
  import moray
  
  # jsから呼び出せるよう登録
  @moray.expose
  def py_func():
      ・・・
  ```
- js_module.js
  ``` javascript
  // 登録されたpythonモジュール読み込み
  import {py_func} from '/moray/py/py_module'
  
  py_func().then(
      value => ・・・
  )
  ```

### Python -> Javascript
- js_module.js
  ``` javascript
  import {expose} from 'moray/js'
  
  // pythonから呼び出せるよう登録
  const js_func() = function() {
    ・・・
  }
  expose(js_func)
  ```
- py_module.py
  ``` python
  from moray.js import js_module
  
  js_module.js_func()
  ```

***
## 参考
- [eel](https://github.com/ChrisKnott/Eel)

