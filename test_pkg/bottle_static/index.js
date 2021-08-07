$(function() {
    if (!window.WebSocket) {
        if (window.MozWebSocket) {
            window.WebSocket = window.MozWebSocket;
        } else {
            $('#result').append("Your browser doesn't support WebSockets.");
        }
    }
    
    var ws = new WebSocket('ws://localhost:8080/websocket');
    ws.onopen = function(evt) {
        $('#result').append('<li>WebSocket connection opened.</li>');
    }
    ws.onmessage = function(evt) {
        $('#result').append('<li>' + evt.data + '</li>');
    }
    ws.onclose = function(evt) {
        $('#result').append('<li>WebSocket connection closed.</li>');
    }
    $('#send').submit(function() {
        ws.send($('input:first').val());
        $('input:first').val('').focus();
        return false;
    });
    $('#message').on('keyup', function() {
        ws.send($('#message').val());
    });
});
