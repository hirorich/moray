const draggable = window.vuedraggable;

export default {
    components: {
        'draggable': draggable
    },
    data() {
        return {
            items: [
                {id: "i_001", name: "n_001"},
                {id: "i_002", name: "n_002"},
                {id: "i_003", name: "n_003"},
            ]
        }
    },
    template: `
<table class="table table-striped table-bordered">
    <thead class="table-dark">
        <tr>
            <th>No</th>
            <th>ID</th>
            <th>NAME</th>
        </tr>
    </thead>
    <draggable tag="tbody" :list="items" item-key="id" handle=".handle" animation=300>
        <template #item="{element, index}">
            <tr>
                <th class="drag-item handle">{{index}}</th>
                <th>{{element.id}}</th>
                <th>{{element.name}}</th>
            </tr>
        </template>
    </draggable>
</table>
    `
};
