import {call_python} from '/error/core.js'
import base_case from '/test_case/base.js'

export default {
    components: {
        'base_case': base_case,
    },
    data() {
        return {
            result: 0,
            title: 'exposeされてない関数呼び出し',
            correct: 'called python function is faild.',
            send_data: '{"id":"ID","method":"call","module":"sample_module.sub_module","func_name":"not_expose","args":[]}',
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
            call_python("ID", this.send_data).then(
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
