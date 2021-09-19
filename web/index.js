import nomal from '/nomal.js'
import nomal_exception from '/nomal_exception.js'
import {expose} from '/moray.js'

const component = {
    components: {
        'nomal': nomal,
        'nomal_exception': nomal_exception,
    },
    template: `
<div class="row">
    <div class="col-6">
        <nomal></nomal>
    </div>
    <div class="col-6">
        <nomal_exception></nomal_exception>
    </div>
</div>
<div class="row">
    <div class="col-6">
    <div><a href="/table/">No WebSocket Page</a></div>
    </div>
    <div class="col-6">
        <div><a href="/error/">異常データ送信系</a></div>
        <div><a href="/unexposed_module/">公開されていないモジュール</a></div>
    </div>
</div>
`
};

const Vue = window.Vue;
const app = Vue.createApp(component);
app.mount('#app');

let log_msg = function(msg) {
    console.log(msg);
    return 'JavaScript: ' + msg
};
expose(log_msg);

let raise_js_exception = function() {
    throw "JavaScript Error"
};
expose(raise_js_exception)
