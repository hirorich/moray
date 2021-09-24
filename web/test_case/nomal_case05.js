import base_case from '/test_case/base.js'
import {return_two} from '/moray/py/sample_module.sub_module.js'

export default {
    components: {
        'base_case': base_case,
    },
    data() {
        return {
            result: 0,
            title: '引数：2、返却値：2',
            correct: [8, 5],
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
            return_two(5, 8).then(
                v => {
                    if (v.length != this.correct.length) {
                        this.result = -1;
                        return
                    }

                    let result = true;
                    for (let i = 0; i < v.length; i++) {
                        result = result && (v[i] == this.correct[i]);
                    }

                    if (result) {
                        this.result = 1;
                    } else {
                        this.result = -1;
                    }
                }
            ).catch(
                v => {
                    this.result = -1;
                }
            );
        },
    },
};
