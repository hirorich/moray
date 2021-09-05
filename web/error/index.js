import {send_msg} from './core.js'

const component = {
    data() {
        return {
            error_data: '{"id": "ID"}',
            unexpose_data: '{"id":"ID","method":"call","module":"sample_module.sub_module","func_name":"not_expose","args":[]}',
        }
    },
    template: `
<div>異常系</div>
<div>異常データ送信</div>
<div>送信データ：{{error_data}}</div>
<button type="button" class="btn btn-danger" @click="send_error_data">send_error_data</button>
<div>exposeされてない関数呼び出し</div>
<div>送信データ：{{unexpose_data}}</div>
<button type="button" class="btn btn-danger" @click="send_unexpose_data">send_unexpose_data</button>
    `,
    methods: {
        send_error_data() {
            send_msg(this.error_data);
        },
        send_unexpose_data() {
            send_msg(this.unexpose_data);
        },
    },
};

const Vue = window.Vue;
const app = Vue.createApp(component);
app.mount('#app');
