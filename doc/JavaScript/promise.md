# Promise
- 非同期処理の最終的な完了もしくは失敗を表すオブジェクト

***
## 目次
- [ざっくりとした概要](#ざっくりとした概要)
- [サンプルコード](#サンプルコード)
  - [基本形](#基本形)
  - [応用形](#応用形)
- [参考](#参考)

***
## ざっくりとした概要
- Promiseとは、JavaScriptにおいて非同期処理の操作が完了したときに結果を返すオブジェクト
  - 非同期処理とは、ある処理が実行されてから終わるまで待たずに次に控えている別の処理を行うこと
- 処理を待機することや、その結果に応じて次の処理をすること約束することができる
- 詳細は以下を参照
  - [Promise](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Promise)
  - [Promiseを使う](https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Using_promises)

***
## サンプルコード
### 基本形
- Promiseオブジェクト生成
``` javascript
// Promiseオブジェクト生成
var my_promise = new Promise((resolve, reject) => {
  console.log('promise');
  try {
    // 時間のかかる処理呼び出し
    let result = my_func();
    resolve(result);
  } catch(e) {
    reject(e);
  }
});

// 成功時のハンドラを付加
my_promise.then((arg) => {
  console.log(arg);
});

// 失敗時のハンドラを付加
my_promise.catch((arg) => {
  console.log(arg);
});

// 完了時のハンドラを付加
my_promise.finally(() => {
  console.log('finally');
});
```
```
>>> promise
```
- my_func() が正常終了した場合
```
>>> [変数resultの内容]
>>> finally
```
- my_func() が異常終了した場合
```
>>> [変数eの内容]
>>> finally
```
- 基本形の等価コード
``` javascript
// Promiseオブジェクト生成
var my_promise = new Promise((resolve, reject) => {
  console.log('promise');
  try {
    // 時間のかかる処理呼び出し
    let result = my_func();
    resolve(result);
  } catch(e) {
    reject(e);
  }
}).then((arg) => {
  console.log(arg);
}).catch((arg) => {
  console.log(arg);
}).finally(() => {
  console.log('finally');
});
```
```
>>> promise
```

### 応用形
- Promiseオブジェクト生成
``` javascript
// Promiseオブジェクト外で成功・失敗ハンドラを呼び出すために宣言
var my_trigger

// Promiseオブジェクト生成
var my_promise = new Promise((resolve, reject) => {
  console.log('promise');
  my_trigger = {resolve: resolve, reject: reject};
}).then((msg) => {
  console.log('then: ' + msg);
}).catch((msg) => {
  console.log('catch: ' + msg);
}).finally(() => {
  console.log('finally');
});
```
```
>>> promise
```
- 成功時のハンドラ呼び出し
``` javascript
my_trigger.resolve('resolve');
```
```
>>> then: resolve
>>> finally
```
- 失敗時のハンドラ呼び出し
``` javascript
my_trigger.reject('reject');
```
```
>>> then: reject
>>> finally
```

***
## 参考
- [Promise](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [【JavaScript】初心者にもわかるPromiseの使い方](https://techplay.jp/column/581)
- [【ES6】 JavaScript初心者でもわかるPromise講座](https://qiita.com/cheez921/items/41b744e4e002b966391a)
