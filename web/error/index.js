import error_case05 from '/test_case/error_case05.js'
import error_case06 from '/test_case/error_case06.js'

const component = {
    components: {
        'error_case05': error_case05,
        'error_case06': error_case06,
    },
    template: `
<div class="container">
    <div class="row">異常系</div>
    <div class="row">
        <div class="col-lg-3 card"><error_case05 /></div>
    </div>
    <div class="row">
        <div class="col-lg-3 card"><error_case06 /></div>
    </div>
</div>
`,
};

const Vue = window.Vue;
const app = Vue.createApp(component);
app.mount('#app');
