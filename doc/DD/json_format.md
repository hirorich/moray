# 送受信jsonデータ定義
- WebSocketで送受信するjsonデータの定義

***
## 目次
- [JavaScript -> Python](#javascript---python)
  - [Python関数呼び出し](#python関数呼び出し)
  - [JavaScript関数の実行結果](#javascript関数の実行結果)
  - [JavaScript関数の公開](#javascript関数の公開)
- [Python -> JavaScript](#python---javascript)
  - [JavaScript関数呼び出し](#javascript関数呼び出し)
  - [Python関数の実行結果](#python関数の実行結果)

***
## JavaScript -> Python
### Python関数呼び出し
``` json
{
    "method": "call",
    "id": JavaScript側で生成されたID,
    "module": 呼び出すPythonモジュール名,
    "func_name": 呼び出すPython関数名,
    "args": 関数の引数リスト
}
```

### JavaScript関数の実行結果
``` json
{
    "method": "return",
    "id": Python側で生成されたID,
    "is_success": 呼び出したJavaScript関数の実行成否(true/false),
    "result": 呼び出したJavaScript関数の実行結果
}
```

### JavaScript関数の公開
``` json
{
    "method": "expose",
    "func_name": 公開するJavaScript関数名
}
```

***
## Python -> JavaScript
### JavaScript関数呼び出し
``` json
{
    "return": false,
    "id": Python側で生成されたID,
    "func_name": 呼び出すJavaScript関数名,
    "args": 関数の引数リスト
}
```

### Python関数の実行結果
``` json
{
    "return": true,
    "id": JavaScript側で生成されたID,
    "is_success": 呼び出したPython関数の実行成否(true/false),
    "result": 呼び出したPython関数の実行結果
}
```
