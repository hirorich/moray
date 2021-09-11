let ws;

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
    ws.onmessage = function(evt) {
        console.log(evt.data);
    }
    ws.onclose = function(evt) {
        console.log('ws.onclose');
    }
};
_init();

// メッセージ送信
let send_msg = function(data) {
    if (ws.readyState == WebSocket.OPEN) {
        ws.send(data);
    }
};

export {send_msg};
