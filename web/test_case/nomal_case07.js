import base_case from '/test_case/base.js'
import {return_tuple} from '/moray/py/sample_module.sub_module.js'

export default {
    components: {
        'base_case': base_case,
    },
    data() {
        return {
            result: 0,
            title: '引数：なし、返却値：タプル',
            correct: [4, 5, 6],
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
            return_tuple().then(
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
                v => {this.result = -1;}
            );
        },
    },
};
