import nomal from '/nomal.js'
import nomal_exception from '/nomal_exception.js'
import moray from '/moray.js'

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

let raise_js_exception2 = function() {
    throw "JavaScript Error"
};
moray.expose(raise_js_exception2)
