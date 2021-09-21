// スタブ
// 本来はサーバ側でモジュール毎に自動生成

export let get_module_name = function() {
    return new Promise((resolve, reject) => {
        resolve('sample_module.sub_module');
    });
}

export let sum = function() {
    return new Promise((resolve, reject) => {
        resolve(13);
    });
}

export let sum_list = function() {
    return new Promise((resolve, reject) => {
        resolve(20);
    });
}

export let log_msg = function() {
    return new Promise((resolve, reject) => {
        resolve('Python: exposed');
    });
}

export let log_msg2 = function() {
    return new Promise((resolve, reject) => {
        resolve("<class 'AttributeError'> '_CLASS' object has no attribute 'log_msg2'");
    });
}

export let return_two = function() {
    return new Promise((resolve, reject) => {
        resolve([8, 5]);
    });
}

export let return_list = function() {
    return new Promise((resolve, reject) => {
        resolve([1, 2, 3]);
    });
}

export let return_tuple = function() {
    return new Promise((resolve, reject) => {
        resolve([4, 5, 6]);
    });
}

export let raise_py_exception = function() {
    return new Promise((resolve, reject) => {
        reject('called python function is faild.');
    });
}

export let raise_js_exception = function() {
    return new Promise((resolve, reject) => {
        reject('called python function is faild.');
    });
}

export let raise_js_exception2 = function() {
    return new Promise((resolve, reject) => {
        resolve("<class 'moray.exception.MorayRuntimeError'> called javascript function is faild.");
    });
}
