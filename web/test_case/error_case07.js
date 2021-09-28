import base_case from '/test_case/base.js'
import {branch_thread} from '/moray/py/tests.module.exposed.js'

export default {
    components: {
        'base_case': base_case,
    },
    data() {
        return {
            result: 0,
            title: '分岐したスレッド内でJavaScript呼び出し',
        }
    },
    template: `
<base_case
    :result="result"
    :title="title"
    :annotation="annotation"
    @on-test="test()
"></base_case>
    `,
    methods: {
        test() {
            branch_thread().then(
                v => {
                    if (v) {
                        this.result = 1;
                    } else {
                        this.result = -1;
                    }
                }
            ).catch(
                v => {this.result = -1;}
            );
        },
    },
};
