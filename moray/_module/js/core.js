let ws;
let call_promise = {};
let unsended_data = [];

let _init = function() {
    if (!window.WebSocket) {
        if (window.MozWebSocket) {
            window.WebSocket = window.MozWebSocket;
        } else {
            console.log("Your browser doesn't support WebSockets.");
        }
    }

    let host = window.location.host;
    ws = new WebSocket('ws://' + host + '/moray/ws');
    ws.onopen = function(evt) {
        for(let i = 0; i < unsended_data.length; i++){
            ws.send(unsended_data.pop());
        }
    }
    ws.onmessage = function(evt) {
        let data = JSON.parse(evt.data);

        if (data.return) {
            if (!(data.id in call_promise)) {
                return;
            }

            if (data.is_success) {
                call_promise[data.id].resolve(data.result);
            } else {
                call_promise[data.id].reject(data.result);
            }
            delete call_promise[data.id];
        }
    }
    ws.onclose = function(evt) {
        console.log('ws.onclose');
    }
};
_init();

// 一意なIDを作成
let uniqueId = function(digits) {
    var strong = typeof digits !== 'undefined' ? digits : 1000;
    return Date.now().toString(16) + Math.floor(strong * Math.random()).toString(16);
};

// メッセージ送信
let send_msg = function(data) {
    if (ws.readyState == WebSocket.OPEN) {
        ws.send(data);
    } else {
        unsended_data.push(data);
    }
};

// pythonを呼び出す
let call_python = function(module, func_name, args) {
    let id = uniqueId();

    let arg_array = [];
    for(let i = 0; i < args.length; i++){
        arg_array.push(args[i]);
    }

    let data = JSON.stringify({
        id: id,
        method: 'call',
        module: module,
        func_name: func_name,
        args: arg_array
    });
    
    return new Promise((reso, reje) => {
        send_msg(data);
        call_promise[id] = {resolve: reso, reject: reje};
    });
};

// javascriptの関数を公開
let expose = function(func) {
    let func_name = func.name;

    let data = JSON.stringify({
        method: 'expose',
        func_name: func_name
    });
    send_msg(data);
}

export {call_python, expose};
