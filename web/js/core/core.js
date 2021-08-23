// 本来はサーバ側で自動生成
// /moray/js/core
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
    
    ws = new WebSocket('ws://localhost:8080/moray/ws');
    ws.onopen = function(evt) {
        console.log('ws.onopen');
        for(let i = 0; i < unsended_data.length; i++){
            ws.send(unsended_data[i]);
        }
    }
    ws.onmessage = function(evt) {
        console.log('ws.onmessage');
        let data = JSON.parse(evt.data);
        if (data.return) {
            call_promise[data.id].resolve(data.result);
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

// pythonを呼び出す
let call_python = function(module, func_name, args) {
    let id = uniqueId();

    let arg_array = [];
    for(let i = 0; i < args.length; i++){
        arg_array.push(args[i]);
    }

    let data = JSON.stringify({
        id: id,
        return: false,
        module: module,
        func_name: func_name,
        args: arg_array
    });
    
    return new Promise((reso, reje) => {
        if (ws.readyState == WebSocket.OPEN) {
            ws.send(data);
        } else {
            unsended_data.push(data);
        }
        call_promise[id] = {resolve: reso, reject: reje};
    });
};

export {call_python};
