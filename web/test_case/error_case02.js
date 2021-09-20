import base_case from '/test_case/base.js'
import {raise_js_exception} from '/moray/py/sample_module.sub_module.js'

export default {
    components: {
        'base_case': base_case,
    },
    data() {
        return {
            result: 0,
            title: 'JavaScript側でエラー',
            correct: 'called python function is faild.',
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
            raise_js_exception().then(
                v => {this.result = -1;}
            ).catch(
                v => {
                    if (v == this.correct) {
                        this.result = 1;
                    } else {
                        this.result = -1;
                    }
                }
            );
        },
    },
};
