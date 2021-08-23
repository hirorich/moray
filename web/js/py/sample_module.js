// 本来はサーバ側でモジュール毎に自動生成
// /moray/py/sample_module
import {call_python} from '/moray/js/core'

export let get_module_name = function() {
    return call_python('my_module', 'get_module_name', arguments);
}

export let sum = function() {
    return call_python('my_module', 'sum', arguments);
}

export let sum_list = function() {
    return call_python('my_module', 'sum_list', arguments);
}