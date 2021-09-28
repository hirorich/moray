import base_case from '/test_case/base.js'
import {raise_js_exception2} from '/moray/py/tests.module.exposed.js'

export default {
    components: {
        'base_case': base_case,
    },
    data() {
        return {
            result: 0,
            title: 'JavaScript側でエラー2',
            correct: "<class 'moray.exception.MorayRuntimeError'> called javascript function is faild.",
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
            raise_js_exception2().then(
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
