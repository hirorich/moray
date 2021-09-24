# logging
- ソフトウェアが実行されているときに起こったイベントを追跡するための標準モジュール

***
## 目次
- [ざっくりとした概要](#ざっくりとした概要)
- [サンプルコード](#サンプルコード)
- [API仕様](#api仕様)
  - [Logger](#logger)
  - [Handler](#handler)
  - [Formatter](#formatter)
  - [fileConfig](#fileconfig)
  - [dictConfig](#dictconfig)
- [参考](#参考)

***
## ざっくりとした概要
ソフトウェアが実行されているときに起こったイベントを追跡するための標準モジュール

ファイルまたはコンソールにログレベルやフォーマットを指定して出力
- 設定は外部ファイル、または以下サンプルコードのようにソースから指定
- 出力するログレベルの指定も可能

標準のログレベルとその適用範囲
- DEBUG
  - おもに問題を診断するときにのみ関心があるような詳細な情報
- INFO
  - 想定された通りのことが起こったことの確認
- WARNING
  - 想定外のことが起こった、または問題が近く起こりそうであることの表示
- ERROR
  - より重大な問題によりソフトウェアがある機能を実行できないこと
- CRITICAL
  - プログラム自体が実行を続けられないことを表す重大なエラー

***
## サンプルコード
``` python
import logging
from logging import FileHandler, Formatter, DEBUG, INFO, ERROR

# フォーマッターを定義
format = '[%(asctime)s][%(levelname)s] %(message)s (at %(name)s:%(lineno)s)'
formatter = Formatter(format)

# ハンドラーを定義（DEBUG）
debug_handler = FileHandler('debug.log', encoding='utf-8')
debug_handler.setLevel(DEBUG)
debug_handler.setFormatter(formatter)

# ハンドラーを定義（ERROR）
error_handler = FileHandler('error.log', encoding='utf-8')
error_handler.setLevel(ERROR)
error_handler.setFormatter(formatter)

# ロガーを定義（INFO）
logger = logging.getLogger(__name__)
logger.addHandler(debug_handler)
logger.addHandler(error_handler)
logger.setLevel(INFO)

# ログ出力
logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')

try:
    raise Exception('raise exception')
except:
    logger.exception('exception')
```
- debug.log
  - ハンドラーのレベルが DEBUG だが、ロガーのレベルが INFO であるため INFO 以上が出力される
``` log
[2021-09-22 11:31:41,446][INFO] info (at __main__:1)
[2021-09-22 11:31:41,446][WARNING] warning (at __main__:1)
[2021-09-22 11:31:41,446][ERROR] error (at __main__:1)
[2021-09-22 11:31:41,461][CRITICAL] critical (at __main__:1)
[2021-09-22 11:31:41,540][ERROR] exception (at __main__:4)
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
Exception: raise exception
```
- error.log
  - ロガーのレベルが INFO だが、ハンドラーのレベルが ERROR であるため ERROR 以上が出力される
``` log
[2021-09-22 11:31:41,446][ERROR] error (at __main__:1)
[2021-09-22 11:31:41,461][CRITICAL] critical (at __main__:1)
[2021-09-22 11:31:41,540][ERROR] exception (at __main__:4)
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
Exception: raise exception
```

***
## API仕様
### [Logger](https://docs.python.org/ja/3/library/logging.html#logging.Logger)
- アプリケーションが実行中にメッセージを記録できるように、いくつかのメソッドをアプリケーションから呼べるようにする
- どのメッセージに対して作用するかをデフォルトのフィルタ機構 またはフィルタオブジェクトに基づいて決定する
- 関心を持っているすべてのログハンドラに、関連するログメッセージを回送する

### [Handler](https://docs.python.org/ja/3/library/logging.html#logging.Handler)
- 適切なログメッセージを (ログメッセージの深刻度に基づいて) ハンドラの指定された出力先に振り分ける 
- Logger オブジェクトには addHandler() メソッドで 0 個以上のハンドラを追加することができる

### [Formatter](https://docs.python.org/ja/3/library/logging.html#logging.Formatter)
- 最終的なログメッセージの順序、構造および内容を設定

### [fileConfig](https://docs.python.org/ja/3/library/logging.config.html#logging.config.fileConfig)
- ファイルからロギング環境設定を取得

### [dictConfig](https://docs.python.org/ja/3/library/logging.config.html#logging.config.dictConfig)
- 辞書からロギング環境設定を取得

***
## 参考
- [Logging HOWTO](https://docs.python.org/ja/3/howto/logging.html)
- [【Python】仕組みを理解してログ出力を使いこなす](https://hackers-high.com/python/logging-overview/)
- [Pythonでprintを卒業してログ出力をいい感じにする](https://qiita.com/FukuharaYohei/items/92795107032c8c0bfd19)
- [[Python] ログ出力フォーマットを設定するには？](https://blog.hiros-dot.net/?p=10328)
