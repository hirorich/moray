// 本来はサーバ側でモジュール毎に自動生成
// /moray/py/sample_module.sub_module
import {send_to_py} from '/moray/js/core'

export let get_module_name = function() {
    return send_to_py('my_module.sub_module', 'get_module_name', arguments);
}

export let sum = function() {
    return send_to_py('my_module.sub_module', 'sum', arguments);
}

export let sum_list = function() {
    return send_to_py('my_module.sub_module', 'sum_list', arguments);
}
