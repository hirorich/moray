import my_table from '/my_table.js'
import my_promise from '/my_promise.js'
import {expose} from '/moray.js'

const component = {
    components: {
        'my-table': my_table,
        'my-promise': my_promise
    },
    template: `
<my-table></my-table>
<my-promise></my-promise>
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
