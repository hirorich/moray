import base_case from '/test_case/base.js'
import {log_msg2} from '/moray/py/sample_module.sub_module.js'

export default {
    components: {
        'base_case': base_case,
    },
    data() {
        return {
            result: 0,
            title: '非公開JavaScript呼び出し',
            correct: "<class 'AttributeError'> module 'moray.js' has no attribute 'log_msg2'",
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
            log_msg2().then(
                v => {
                    if (v == this.correct) {
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
