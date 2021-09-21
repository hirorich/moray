import {call_python} from '/error/core.js'
import base_case from '/test_case/base.js'

export default {
    components: {
        'base_case': base_case,
    },
    data() {
        return {
            result: 0,
            title: '異常データ送信',
            annotation: 'ログに "internal error has occurred." が出力されること',
            send_data: '{"id": "ID"}',
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
            call_python("ID", this.send_data).then(
                v => {this.result = -1;}
            ).catch(
                v => {this.result = -1;}
            );
            this.result = 1;
        },
    },
};
