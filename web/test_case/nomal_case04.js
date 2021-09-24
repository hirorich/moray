import base_case from '/test_case/base.js'
import {log_msg} from '/moray/py/sample_module.sub_module.js'

export default {
    components: {
        'base_case': base_case,
    },
    data() {
        return {
            result: 0,
            title: '引数：なし、返却値：なし',
        }
    },
    template: `
<base_case
    :result="result"
    :title="title"
    @on-test="test()
"></base_case>
    `,
    methods: {
        test() {
            log_msg().then(
                v => {this.result = 1;}
            ).catch(
                v => {this.result = -1;}
            );
        },
    },
};
