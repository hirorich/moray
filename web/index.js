import nomal_exception from '/nomal_exception.js'
import moray from '/moray.js'
import nomal_case01 from '/test_case/nomal_case01.js'
import nomal_case02 from '/test_case/nomal_case02.js'
import nomal_case03 from '/test_case/nomal_case03.js'
import nomal_case04 from '/test_case/nomal_case04.js'
import nomal_case05 from '/test_case/nomal_case05.js'
import nomal_case06 from '/test_case/nomal_case06.js'
import nomal_case07 from '/test_case/nomal_case07.js'

const component = {
    components: {
        'nomal_exception': nomal_exception,
        'nomal_case01': nomal_case01,
        'nomal_case02': nomal_case02,
        'nomal_case03': nomal_case03,
        'nomal_case04': nomal_case04,
        'nomal_case05': nomal_case05,
        'nomal_case06': nomal_case06,
        'nomal_case07': nomal_case07,
    },
    template: `
<div class="container">
<div class="row">正常系</div>
<div class="row">
    <div class="col-lg-3"><nomal_case01 /></div>
    <div class="col-lg-3"><nomal_case02 /></div>
    <div class="col-lg-3"><nomal_case03 /></div>
    <div class="col-lg-3"><nomal_case04 /></div>
    <div class="col-lg-3"><nomal_case05 /></div>
    <div class="col-lg-3"><nomal_case06 /></div>
    <div class="col-lg-3"><nomal_case07 /></div>
</div>
</div>
<div class="row">
    <div class="col-6">
        <nomal_exception></nomal_exception>
    </div>
</div>
<div class="row">
    <div class="col-6">
    <div><a href="/other_ws/">Other WebSocket Page</a></div>
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
moray.expose(log_msg);

let raise_js_exception = function() {
    throw "JavaScript Error"
};
moray.expose(raise_js_exception)

moray.onclose = function(evt) {
    alert('moray closed');
};
