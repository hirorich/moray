# moray ナレッジドキュメント
- moray作成のために調査したものを区切りごとにナレッジとして残す
- 技術的な仕組みよりも使い方がメイン

***
## 目次
- [Python](#python)
- [JavaScript](#javascript)
- [moray](#moray)
- [github](#github)

***
## Python
### [Docstring](Python/docstring_google.md)
- Pythonにおけるクラスやメソッド(関数)についての説明を記載したコメント文

### [decorator](Python/decorator.md)
- 通常 @wrapper 構文で関数変換として適用される別の関数を返す関数

### [unittest](Python/unittest.md)
- JUnitに触発されたPythonのユニットテストフレームワーク

### [Pythonプロジェクトをパッケージ化する方法](Python/packaging.md)
- シンプルなPythonプロジェクトをパッケージ化する方法のチュートリアル

### [logging](Python/logging.md)
- ソフトウェアが実行されているときに起こったイベントを追跡するための標準モジュール

### [Bottle](Python/bottle.md)
- Python用のWSGIマイクロWebフレームワーク

### [WebSocket](Python/websocket.md)
- クライアントとサーバの双方向通信を可能にする、単一のTCPコネクション上のプロトコル

### [jinja2](Python/jinja2.md)
- 高速で表現力豊かな拡張可能なテンプレート・エンジン

***
## JavaScript
### [Promise](JavaScript/promise.md)
- 非同期処理の最終的な完了もしくは失敗を表すオブジェクト

***
## moray
### [基本設計](moray/basic_design_doc.md)
- 機能一覧とPython・JavaScript間の相互呼び出し

### 詳細設計
- [Python編](moray/detailed_design_doc/dd_python.md)
  - Python側の詳細設計
- [JavaScript編](moray/detailed_design_doc/dd_javascript.md)
  - JavaScript側の詳細設計

### [送受信jsonデータ定義](moray/json_format.md)
- WebSocketで送受信するjsonデータの定義

***
## github
### [リポジトリへのライセンスの追加](https://docs.github.com/ja/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)
- 外部リンク
