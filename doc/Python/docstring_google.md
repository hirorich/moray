# Docstring
- Pythonにおけるクラスやメソッド(関数)についての説明を記載したコメント文
- 変数__doc__に格納されている
- Docstringの記法にはreStructuredTextスタイル，Numpyスタイル，Googleスタイルの3つがある
  - 本ドキュメントではGoogleスタイルについて記載

***
## 目次
- [サンプルコード](#サンプルコード)
- [記載方法](#記載方法)
  - [モジュール](#モジュール)
  - [クラス](#クラス)
  - [関数](#関数)
- [セクション](#セクション)
  - [ToDo](#ToDo)
  - [Attributes](#Attributes)
  - [Args](#Args)
  - [Returns](#Returns)
  - [Yields](#Yields)
  - [Raises](#Raises)
  - [Examples](#Examples)
  - [Note](#Note)
- [参考](#参考)

***
## サンプルコード
``` python
""" モジュールの説明タイトル
モジュールについての説明文

Todo:
    TODOリストを記載

"""

import xxx

class TestClass() :
    """ クラスの説明タイトル
    クラスについての説明文
    
    Attributes:
        属性の名前 (属性の型): 属性の説明
        属性の名前 (:obj:`属性の型`): 属性の説明
    
    """
    
    def test_func(self, param1, param2=None) :
        """ 関数の説明タイトル
        関数についての説明文
        
        Args:
            引数の名前 (引数の型): 引数の説明
            引数の名前 (:obj:`引数の型`, optional): 引数の説明
        
        Returns:
            戻り値の型: 戻り値の説明
                (例: True なら成功, False なら失敗)
        
        Yields:
            戻り値の型: 戻り値についての説明
        
        Raises:
            例外の名前: 例外の説明
                (例: 引数が指定されていない場合に発生 )
        
        Examples:
            関数の使い方について記載
            >>> print_test ("test", "message")
                test message
        
        Note:
            注意事項などを記載
        
        """
```

***
## 記載方法
- コメントを複数行のコメントブロック「"""」で囲む
- 「"""」の右隣にタイトルを記載できる
- 対象はモジュール、クラス、関数の3つ

### モジュール
- モジュールの説明を記載
- ソースコードの冒頭に記載
  - コメント文を除いたソースコードの一番始め
  - importよりも前

### クラス
- クラスの説明を記載
- クラス定義の下の行に記載

### 関数
- 関数の説明を記載
- 関数定義の下の行に記載

***
## セクション
### ToDo
- Todoリストを記載するセクション
- 実装予定の処理など、後から実施する作業を記載

### Attributes
- クラスの属性の説明を記載するセクション
  - 属性の型、名前など

### Args
- 引数の説明を記載するセクション
  - 名前、型、省略可能(optional)など
- インスタンスを示すselfは省略
- 省略可能な引数はoptionalを記載

### Returns
- retrun文を使用した関数の戻り値を記載するセクション

### Yields
- yeild文を使用した関数の戻り値を記載するセクション

### Raises
- 例外処理に対する説明を記載するセクション

### Examples
- 関数、クラスの実行例について記載するセクション
- ExamplesではなくExampleでも良い

### Note
- 注釈について記載するセクション

***
## 参考
- [GoogleスタイルのPython Docstringの入門](https://qiita.com/11ohina017/items/118b3b42b612e527dc1d)
