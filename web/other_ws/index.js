import nomal_case01 from '/test_case/nomal_case01.js'
import error_case05 from '/test_case/error_case05.js'

const component = {
    components: {
        'nomal_case01': nomal_case01,
        'error_case05': error_case05,
    },
    template: `
<div class="container">
    <div class="row">正常系</div>
    <div class="row">
        <div class="col-lg-3 card"><nomal_case01 /></div>
    </div>
    <div class="row">異常系</div>
    <div class="row">
        <div class="col-lg-3 card"><error_case05 /></div>
    </div>
</div>
`
};

const Vue = window.Vue;
const app = Vue.createApp(component);
app.mount('#app');
