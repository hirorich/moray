import nomal_case01 from '/test_case/nomal_case01.js'
import error_case04 from '/test_case/error_case04.js'

const component = {
    components: {
        'nomal_case01': nomal_case01,
        'error_case04': error_case04,
    },
    template: `
<div class="container">
    <div class="row">正常系</div>
    <div class="row">
        <div class="col-lg-3 card"><nomal_case01 /></div>
    </div>
    <div class="row">異常系</div>
    <div class="row">
        <div class="col-lg-3 card"><error_case04 /></div>
    </div>
</div>
`
};

const Vue = window.Vue;
const app = Vue.createApp(component);
app.mount('#app');
