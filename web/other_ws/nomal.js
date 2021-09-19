import {get_module_name, sum, sum_list, log_msg, return_two, return_list, return_tuple} from '/moray/py/sample_module.sub_module.js'

export default {
    data() {
        return {
            data: '返却値'
        }
    },
    template: `
<div>正常系</div>
<div>{{data}}</div>
<div>引数：なし、返却値：1</div>
<button type="button" class="btn btn-success" @click="get_module_name">get_module_name</button>
<div>引数：2、返却値：1</div>
<button type="button" class="btn btn-success" @click="sum">sum</button>
<div>引数：リスト、返却値：1</div>
<button type="button" class="btn btn-success" @click="sum_list">sum_list</button>
<div>引数：なし、返却値：なし</div>
<button type="button" class="btn btn-success" @click="log_msg">log_msg</button>
<div>引数：2、返却値：2</div>
<button type="button" class="btn btn-success" @click="return_two">return_two</button>
<div>引数：なし、返却値：リスト</div>
<button type="button" class="btn btn-success" @click="return_list">return_list</button>
<div>引数：なし、返却値：タプル</div>
<button type="button" class="btn btn-success" @click="return_tuple">return_tuple</button>
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
        log_msg() {
            log_msg();
        },
        return_two() {
            return_two(5, 8).then(
                v => {
                    var result = "";
                    v.forEach(a => {
                        result += String(a) + ", ";
                    });
                    this.data = result;
                }
            );
        },
        return_list() {
            return_list().then(
                v => {
                    var result = "";
                    v.forEach(a => {
                        result += String(a) + ", ";
                    });
                    this.data = result;
                }
            );
        },
        return_tuple() {
            return_tuple().then(
                v => {
                    var result = "";
                    v.forEach(a => {
                        result += String(a) + ", ";
                    });
                    this.data = result;
                }
            );
        },
    },
};
