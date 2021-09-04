// スタブ
// 本来はサーバ側でモジュール毎に自動生成

export let get_module_name = function() {
    return new Promise((resolve, reject) => {
        resolve('stub: get_module_name');
    });
}

export let sum = function() {
    return new Promise((resolve, reject) => {
        resolve(9);
    });
}

export let sum_list = function() {
    return new Promise((resolve, reject) => {
        resolve(64);
    });
}

export let log_msg = function() {
    return new Promise((resolve, reject) => {
        resolve('Python: exposed');
    });
}

export let return_two = function() {
    return new Promise((resolve, reject) => {
        resolve([6, 4]);
    });
}

export let return_list = function() {
    return new Promise((resolve, reject) => {
        resolve([1, 2, 3]);
    });
}

export let return_tuple = function() {
    return new Promise((resolve, reject) => {
        resolve([9, 8, 7]);
    });
}
