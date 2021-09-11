import {raise_py_exception, raise_js_exception} from '/moray/py/sample_module.sub_module.js'

export default {
    data() {
        return {
            data: '返却値'
        }
    },
    template: `
<div>異常系</div>
<div>{{data}}</div>
<div>Python側でエラー</div>
<button type="button" class="btn btn-danger" @click="raise_py_exception">raise_py_exception</button>
<div>JavaScript側でエラー</div>
<button type="button" class="btn btn-danger" @click="raise_js_exception">raise_js_exception</button>
    `,
    methods: {
        raise_py_exception() {
            raise_py_exception().then(
                v => {this.data = "Success: " + v}
            ).catch(
                v => {this.data = "Error: " + v}
            );
        },
        raise_js_exception() {
            raise_js_exception().then(
                v => {this.data = "Success: " + v}
            ).catch(
                v => {this.data = "Error: " + v}
            );
        },
    },
};
