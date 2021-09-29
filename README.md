# moray
**<span>README</span>.md is a translation of README_jp.md.**

- Package for creating HTML GUI using Python modules and JavaScript.
- Managing Python functions in modules.

***
## Contents
- [Install](#install)
- [Directory Structure](#directory-structure)
- [Usage](#usage)
  - [Starting the app](#starting-the-app)
  - [App options](#app-options)
  - [Call Python from JavaScript](#call-python-from-javascript)
  - [Call JavaScript from Python](#call-javascript-from-python)
  - [Abnormal exit handler](#abnormal-exit-handler)
  - [Logging](#logging)
- [Packages using](#packages-using)

***
## Install
- Execute the following command.
  ```
  pip install moray
  ```

***
## Directory Structure
- The moray application consists of a front-end with .html, .js, .css, etc., and a back-end with Python scripts.
- **/moray.js and /moray/ cannot be used, because moray use them.**
  ```
  python_script.py     <-- Python script
  web/                 <-- static web directory
    index.html
    css/
      style.css
    img/
      logo.png
  ```

***
## Usage
### Starting the app
- Suppose you put all the frontend files in `web` directory, including your start page `index.html`, then the app is started like this.
  ``` python
  import moray
  
  moray.run('web')
  ```
    - This will open a browser to `http://localhost:<automatically picked port>/index.html`.

### App options
- Additional options can be passed to `moray.run()` as keyword arguments.
  - start_page
    - str type (Default: '')
    - Your start page.
      - If `''`, index.html will be opened.
  - host
    - str type (Default: 'localhost')
    - Hostname to use for the Bottle server.
      - `'localhost'` or IP address is allowed.
  - port
    - int type (Default: 0)
    - Port to use for the Bottle server.
      - `0` or a value between `1025` and `65535` is allowed.
  - browser
    - str type (Default: 'chrome')
    - Browser to use.
      - Only `'chrome'` can be used.
  - cmdline_args
    - list of str type (Default: [])
    - Command line arguments to start the browser.
  - position
    - tuple of 2 int type (Default: None)
    - The (left, top) of the main window in pixels.
      - If not specified, `None`.
  - size
    - tuple of 2 int type (Default: None)
    - The (width, height) of the main window in pixels.
      - If not specified, `None`.

- Example
  ``` python
  import moray
  
  moray.run(
      'web',
      start_page = 'index.html',
      host = 'localhost',
      port = 8000,
      browser = 'chrome',
      cmdline_args = ['--disable-http-cache', '--incognito'],
      position = (400, 200),
      size = (800, 600)
  )
  ```

### Call Python from JavaScript
- **Python関数の呼び出しごとに別スレッド上で動作する**
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

### Call JavaScript from Python
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

### Abnormal exit handler
- 不測の事態によりmorayが終了してしまった場合 moray.onclose によって終了したことを検知可能
- js_module.js
  ``` javascript
  import moray from '/moray.js'
  
  // moray.onclose に関数を登録する
  // evt には null が渡される
  moray.onclose = function(evt) {
      alert('moray closed');
  }
  ```

### Logging
- moray 内では logging モジュールによるログ出力を行うため、 moray モジュールに対してロガーを設定することでロギング可能
- ロガー設定例
  ``` python
  import logging
  
  format = '[%(asctime)s][%(levelname)s] %(message)s (at %(name)s:%(lineno)s)'
  formatter = logging.Formatter(format)
  
  handler = logging.StreamHandler()
  handler.setLevel(logging.DEBUG)
  handler.setFormatter(formatter)
  
  logger = logging.getLogger('moray')
  logger.addHandler(handler)
  logger.setLevel(logging.INFO)
  ```

***
## Packages using
- [bottle-websocket](https://pypi.org/project/bottle-websocket/)
  - [MIT License](https://github.com/zeekay/bottle-websocket/blob/master/LICENSE)
- [requests](https://pypi.org/project/requests/)
  - [Apache License 2.0](https://github.com/psf/requests/blob/main/LICENSE)
- [Jinja2](https://pypi.org/project/Jinja2/)
  - [BSD License (BSD-3-Clause)](https://github.com/pallets/jinja/blob/main/LICENSE.rst)
