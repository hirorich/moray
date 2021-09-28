import {not_expose} from '/moray/py/tests.module.unexposed.js'

const component = {
    data() {
        return {
            data: '返却値'
        }
    },
    template: `
<div>正常系</div>
<div>{{data}}</div>
<div>引数：なし、返却値：1</div>
<button type="button" class="btn btn-danger" @click="not_expose">not_expose</button>
    `,
    methods: {
        not_expose() {
            not_expose().then(
                v => {this.data = v}
            );
        },
    },
};

const Vue = window.Vue;
const app = Vue.createApp(component);
app.mount('#app');
