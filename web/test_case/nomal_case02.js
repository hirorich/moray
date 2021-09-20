import base_case from '/test_case/base.js'
import {sum} from '/moray/py/sample_module.sub_module.js'

export default {
    components: {
        'base_case': base_case,
    },
    data() {
        return {
            result: 0,
            title: '引数：2、返却値：1',
            correct: 13,
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
            sum(5, 8).then(
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
