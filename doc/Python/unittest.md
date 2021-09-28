# unittest
- JUnitに触発されたPythonのユニットテストフレームワーク

***
## 目次
- [ざっくりとした概要](#ざっくりとした概要)
- [サンプルコード](#サンプルコード)
- [API仕様](#api仕様)
  - [assertEqual](#assertequal)
  - [assertRaises](#assertraises)
  - [fail](#fail)
  - [mock.patch](#mockpatch)
  - [mock.MagicMock](#mockmagicmock)
- [参考](#参考)

***
## ざっくりとした概要
テストの自動化、テスト用のセットアップやシャットダウンのコードの共有、テストのコレクション化、報告フレームワークからのテストの独立性をサポート

以下の概念をオブジェクト指向でサポートすることにより実現される
- テストフィクスチャ (test fixture)
  - 1つまたは複数のテストを実行するために前処理と後処理
    - 一時ディレクトリ作成、サーバープロセス起動など
- テストケース (test case)
  - テストの独立した単位で、各入力に対する結果をチェック
  - unittest.TestCase クラスを基底クラスとしてテストケースを作成する
- テストスイート (test suite)
  - テストケースとテストスイートの集まり
  - 同時に実行しなければならないテストをまとめる場合に使用
- テストランナー (test runner)
  - テストの実行を管理し結果を提供する要素

unittest.mock によるモックの作成も可能

***
## サンプルコード
- モック化対象モジュール
``` python
"""
my_package\sub_module.py
"""

_items = [1, 2, 3]

def func():
    
    sum = 0
    for item in _items:
        sum += item
    
    return sum

class Class():
    
    _bool = False
    
    def get_bool(self):
        return self._bool
```
- テスト対象モジュール
``` python
"""
my_package\my_module.py
"""
from my_package import sub_module

def func():
    
    return sub_module.func()

def class_func():
    
    instance = sub_module.Class()
    return instance.get_bool()
```
- テストケース
``` python
"""
test\test_my_module.py
"""
import unittest
from unittest.mock import patch, MagicMock

from my_package import my_module

class MyModuleTest(unittest.TestCase):
    
    @patch('my_package.sub_module.func', MagicMock(return_value = 15))
    def test_func(self):
        self.assertEqual(my_module.func(), 15)
    
    def test_class_func(self):
        with patch('my_package.sub_module.Class.get_bool', MagicMock(return_value = True)) as get_bool:
            self.assertEqual(my_module.class_func(), True)
```
- .vscode\setting.json
  - testsフォルダ直下の test_ から始まるモジュールがテストケースである場合
``` json
{
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./tests",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.unittestEnabled": true,
}
```

***
## API仕様
### [assertEqual](https://docs.python.org/ja/3/library/unittest.html#unittest.TestCase.assertEqual)
``` python
assertEqual(first, second, msg=None)
```
- first と second が等しいことをテスト

### [assertRaises](https://docs.python.org/ja/3/library/unittest.html#unittest.TestCase.assertRaises)
``` python
assertRaises(exception, callable, *args, **kwds)
assertRaises(exception, *, msg=None)
```
- callable を呼び出した時に例外が発生することをテスト

### [fail](https://docs.python.org/ja/3/library/unittest.html#unittest.TestCase.fail)
- 無条件にテストを失敗させる

### [mock.patch](https://docs.python.org/ja/3/library/unittest.mock.html#unittest.mock.patch)
- with句またはデコレータ内にモックを適用する
- モック対象はimportできる形でパスを指定する必要がある

### [mock.MagicMock](https://docs.python.org/ja/3/library/unittest.mock.html#unittest.mock.MagicMock)
- アクセスしたすべての属性とメソッドを作成
- どのように使用されたかについての詳細な情報を格納
``` python
MagicMock('abc')
```
- 変数に対するモック
``` python
MagicMock(return_value=3)
```
- 関数に対するモック
``` python
MagicMock(side_effect=[1, 2, 3])
```
- 呼び出すごとに異なる値を返させたい場合の関数に対するモック
``` python
MagicMock(side_effect=KeyError('foo'))
```
- 任意のエラーを発生させる

***
## 参考
- [unittest --- ユニットテストフレームワーク](https://docs.python.org/ja/3/library/unittest.html)
- [unittest.mock --- モックオブジェクトライブラリ](https://docs.python.org/ja/3/library/unittest.mock.html)
- [Python testing in Visual Studio Code](https://code.visualstudio.com/docs/python/testing)
- [Visual Studio CodeでのPython単体テストが便利すぎる件](https://hiroronn.hatenablog.jp/entry/20180905/1536146652)
