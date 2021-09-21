// WebSocketオブジェクト
let ws;

// 呼び出し中データ
let calling_promise = {};

// 未送信データ
let unsended_data = [];

let _init = function() {
    if (!window.WebSocket) {
        if (window.MozWebSocket) {
            window.WebSocket = window.MozWebSocket;
        } else {
            alert("Your browser doesn't support WebSockets.");
        }
    }

    let host = window.location.host;
    ws = new WebSocket('ws://' + host + '/moray/ws');
    ws.onopen = function(evt) {

        // 未送信データを送信
        let data_length = unsended_data.length;
        for(let i = 0; i < data_length; i++){
            ws.send(unsended_data.pop());
        }
    }
    ws.onmessage = function(evt) {
        let data = JSON.parse(evt.data);

        // 呼び出したPythonからの返却値の場合
        if (data.return) {
    
            // IDを確認
            if (!(data.id in calling_promise)) {
                return;
            }
    
            // 成否結果をPromise結果に登録
            if (data.is_success) {
                calling_promise[data.id].resolve(data.result);
            } else {
                calling_promise[data.id].reject(data.result);
            }
            delete calling_promise[data.id];
        } else {
            alert('aaaa');
        }
    }
    ws.onclose = function(evt) {
        alert('ws.onclose');
    }
};
_init();

// メッセージ送信
let send_msg = function(data) {
    if (ws.readyState == WebSocket.OPEN) {
        ws.send(data);
    } else {
        unsended_data.push(data);
    }
};

// pythonを呼び出す
let call_python = function(id, data) {

    // Python側にデータ送信
    return new Promise((reso, reje) => {
        send_msg(data);
        calling_promise[id] = {resolve: reso, reject: reje};
    });
}

export {call_python};
