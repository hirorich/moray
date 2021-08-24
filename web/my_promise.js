import {get_module_name, sum, sum_list} from '/moray/py/sample_module.js'

export default {
    data() {
        return {
            data: 'my_promise'
        }
    },
    template: `
<div>{{data}}</div>
<button type="button" class="btn btn-primary" @click="get_module_name">get_module_name</button>
<button type="button" class="btn btn-success" @click="sum">sum</button>
<button type="button" class="btn btn-info" @click="sum_list">sum_list</button>
    `,
    methods: {
        get_module_name() {
            get_module_name().then(
                v => {this.data = v}
            );
        },
        sum() {
            sum(5, 8).then(
                v => {this.data = v}
            );
        },
        sum_list() {
            sum_list([2, 7, 11]).then(
                v => {this.data = v}
            );
        },
    },
};
