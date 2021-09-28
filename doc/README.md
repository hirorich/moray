# moray開発メモ

***
## 目次
- [経緯](#経緯)
- [開発環境構築](#開発環境構築)
- [設計](#設計)
- [ビルド](#ビルド)
- [参考](#参考)

***
## 経緯
- PythonによるGUI作成のライブラリのうち、eelがJavaScriptでGUIを作成できるため愛用していた
- しかし、eelによるPythonの関数管理は関数名により行われるため、名前かぶりがないように管理するのが面倒
- よって、モジュールも含めて管理することで名前被りを防ぐよう対応する

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
  - [MIT License](https://github.com/zeekay/bottle-websocket/blob/master/LICENSE)
  - bottleでWebSocketを使用するためのプラグイン
  - 以下を実行することでインストール
    ``` bash
    pip install bottle-websocket
    ```
- [bottle](https://pypi.org/project/bottle/)
  - [MIT License](https://bottlepy.org/docs/dev/#license)
  - 軽量Webフレームワーク
  - bottle-websocketの依存ライブラリ
  - bottle-websocketインストール時にインストール
- [gevent-websocket](https://pypi.org/project/gevent-websocket/)
  - [Apache License 2.0](https://gitlab.com/noppo/gevent-websocket/-/blob/master/LICENSE)
  - bottle-websocketの依存ライブラリ
  - bottle-websocketインストール時にインストール
- [gevent](https://pypi.org/project/gevent/)
  - [MIT License](https://github.com/gevent/gevent/blob/master/LICENSE)
  - gevent-websocketの依存ライブラリ
  - bottle-websocketインストール時にインストール
- [requests](https://pypi.org/project/requests/)
  - [Apache License 2.0](https://github.com/psf/requests/blob/main/LICENSE)
  - サーバ起動確認に使用
  - 以下を実行することでインストール
    ``` bash
    pip install requests
    ```
- [Jinja2](https://pypi.org/project/Jinja2/)
  - [BSD License (BSD-3-Clause)](https://github.com/pallets/jinja/blob/main/LICENSE.rst)
  - テンプレートエンジン
  - 以下を実行することでインストール
    ``` bash
    pip install Jinja2
    ```

***
## 設計
- [plantUML](https://plantuml.com/ja/)

### [基本設計](BD/README.md)
- 機能一覧とPython・JavaScript間の相互呼び出し

### 詳細設計
- [Python編](DD/python.md)
  - Python側の詳細設計
- [JavaScript編](DD/javascript.md)
  - JavaScript側の詳細設計
- [送受信jsonデータ定義](DD/json_format.md)
  - WebSocketで送受信するjsonデータの定義

### テスト
- unittest を使用
- テスト資源は tests フォルダ配下に配置
- 結合テストは `doc\test.bat` または以下コマンドによりテスト用アプリ起動
  ```
  python -m tests
  ```

***
## ビルド
```
python -m pip install --upgrade build
python -m build
```

***
## 参考
- [eel](https://github.com/ChrisKnott/Eel)

