# decorator
- 通常 @wrapper 構文で関数変換として適用される別の関数を返す関数

***
## 目次
- [ざっくりとした概要](#ざっくりとした概要)
- [サンプルコード](#サンプルコード)
- [API仕様](#api仕様)
- [参考](#参考)

***
## ざっくりとした概要
通常 @wrapper 構文で関数変換として適用される別の関数を返す関数

関数定義は一つ以上のデコレータ式でラップ可能

同様にクラスもデコレート可能

***
## サンプルコード
- 引数なしデコレータ
``` python
from functools import wraps

def deco(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('--start--')
        f(*args, **kwargs)
        print('--end--')
    return wrapper

@deco
def func(msg):
    print(msg)

func('Hello Decorator')
```
```
--start--
Hello Decorator
--end--
```

- 引数ありデコレータ
``` python
from functools import wraps

def deco(a, b):
    def _deco(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print('a: {0}, b: {1}'.format(a, b))
            f(*args, **kwargs)
        return wrapper
    return _deco

@deco('abc', '123')
def func(msg):
    print(msg)

func('Hello Decorator')
```
```
a: abc, b: 123
Hello Decorator
```

- 返却値ありデコレータ
``` python
from functools import wraps

def deco(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs) * 3
    return wrapper

@deco
def func(a, b):
    return a + b

print(func(1, 2))
```
```
9
```

- @wraps(f) 適用あり
``` python
from functools import wraps

def deco(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        """
        wrapper docstring
        """
        return f(*args, **kwargs)
    return wrapper

@deco
def func(msg):
    """
    func docstring
    """
    pass

print(func.__doc__)
```
```
func docstring
```

- @wraps(f) 適用なし
``` python
def deco(f):
    def wrapper(*args, **kwargs):
        """
        wrapper docstring
        """
        return f(*args, **kwargs)
    return wrapper

@deco
def func(msg):
    """
    func docstring
    """
    pass

print(func.__doc__)
```
```
wrapper docstring
```
***
## API仕様

***
## 参考
- [decorator](https://docs.python.org/ja/3/glossary.html#term-decorator)
- [関数定義](https://docs.python.org/ja/3/reference/compound_stmts.html#function)
- [クラス定義](https://docs.python.org/ja/3/reference/compound_stmts.html#class)
- [Pythonのデコレータを理解するための12Step](https://qiita.com/_rdtr/items/d3bc1a8d4b7eb375c368)
- [Pythonのデコレータについて](https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e)
