// 本来はサーバ側でモジュール毎に自動生成
// /moray/py/my_module
import {send_to_py} from '/moray/core/core'

export let py_func = function() {
    return send_to_py('my_module', 'py_func', arguments);
}

export let py_func2 = function() {
    return send_to_py('my_module', 'py_func2', arguments);
}
