import moray from '/moray.js'
import nomal_case01 from '/test_case/nomal_case01.js'
import nomal_case02 from '/test_case/nomal_case02.js'
import nomal_case03 from '/test_case/nomal_case03.js'
import nomal_case04 from '/test_case/nomal_case04.js'
import nomal_case05 from '/test_case/nomal_case05.js'
import nomal_case06 from '/test_case/nomal_case06.js'
import nomal_case07 from '/test_case/nomal_case07.js'
import error_case01 from '/test_case/error_case01.js'
import error_case02 from '/test_case/error_case02.js'
import error_case03 from '/test_case/error_case03.js'
import error_case07 from '/test_case/error_case07.js'

const component = {
    components: {
        'nomal_case01': nomal_case01,
        'nomal_case02': nomal_case02,
        'nomal_case03': nomal_case03,
        'nomal_case04': nomal_case04,
        'nomal_case05': nomal_case05,
        'nomal_case06': nomal_case06,
        'nomal_case07': nomal_case07,
        'error_case01': error_case01,
        'error_case02': error_case02,
        'error_case03': error_case03,
        'error_case07': error_case07,
    },
    template: `
<div class="container">
    <div class="row">正常系</div>
    <div class="row">
        <div class="col-lg-3 card"><nomal_case01 /></div>
        <div class="col-lg-3 card"><nomal_case02 /></div>
        <div class="col-lg-3 card"><nomal_case03 /></div>
        <div class="col-lg-3 card"><nomal_case04 /></div>
        <div class="col-lg-3 card"><nomal_case05 /></div>
        <div class="col-lg-3 card"><nomal_case06 /></div>
        <div class="col-lg-3 card"><nomal_case07 /></div>
    </div>
    <div class="row">異常系</div>
    <div class="row">
        <div class="col-lg-3 card"><error_case01 /></div>
        <div class="col-lg-3 card"><error_case02 /></div>
        <div class="col-lg-3 card"><error_case03 /></div>
        <div class="col-lg-3 card"><error_case07 /></div>
    </div>
    <div class="row">画面遷移</div>
    <div class="row">
        <div class="col-lg-6 card">
            <h6 class="card-title">別morayページ遷移</h6>
            <div class="card-body">
                <div><a href="/other_ws/">ページ遷移</a></div>
            </div>
        </div>
        <div class="col-lg-6 card">
            <h6 class="card-title">非morayページ遷移</h6>
            <div class="card-body">
                <div>別ウィンドウでない場合はサーバ終了</div>
                <div><a href="/table/">ページ遷移</a></div>
            </div>
        </div>
        <div class="col-lg-6 card">
        <h6 class="card-title">異常データ送信系</h6>
            <div class="card-body">
                <div><a href="/error/">ページ遷移</a></div>
            </div>
        </div>
        <div class="col-lg-6 card">
            <h6 class="card-title">非公開モジュール(正常に画面が表示されない)</h6>
            <div class="card-body">
                <div>別ウィンドウでない場合はサーバ終了</div>
                <div><a href="/unexposed_module/">ページ遷移</a></div>
            </div>
        </div>
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
