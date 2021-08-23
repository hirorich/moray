import my_table from '/my_table.js'
import my_promise from '/my_promise.js'

const component = {
    components: {
        'my-table': my_table,
        'my-promise': my_promise
    },
    template: `
<my-table></my-table>
<my-promise></my-promise>
`
};

const Vue = window.Vue;
const app = Vue.createApp(component);
app.mount('#app');