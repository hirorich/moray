export default {
    props: {
        result: Number,
        title: String,
        annotation: String,
    },
    template: `
<h6 class="card-title">{{title}}</h6>
<div class="card-body">
    <div>{{annotation}}</div>
    <button type="button" class="btn btn-primary" @click="$emit('onTest')">テスト実行</button>
    <span v-if="result==1">〇</span>
    <span v-else-if="result==-1">×</span>
    <span v-else>－</span>
</div>
`,
};
