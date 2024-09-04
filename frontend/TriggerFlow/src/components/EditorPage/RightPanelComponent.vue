<template>
    <div class="card flex flex-col h-full">
        <Listbox v-model="selectedCode" :options="codeSnippets" optionLabel="name" listStyle="max-height:1000px" filter class="flex-grow">
            <template #option="slotProps">
                <div 
                    class="flex items-center cursor-move" 
                    draggable="true" 
                    @dragstart="onDragStart($event, slotProps.option)"
                    v-tooltip.left="{ value: slotProps.option.description, showDelay: 1000, hideDelay: 200 }"
                >
                    {{ slotProps.option.name }}
                </div>
            </template>
        </Listbox>
    </div>  
</template>

<script setup>
import { ref } from "vue";
import Listbox from 'primevue/listbox';
import Tooltip from 'primevue/tooltip';

const props = defineProps({
    codeSnippets: {
        type: Array, 
        required: true
    }
});

const emit = defineEmits(['drag-start']);

const selectedCode = ref();

const onDragStart = (event, item) => {
    event.dataTransfer.setData('text/plain', JSON.stringify(item));
    emit('drag-start', item);
};
</script>

<style scoped>
.p-listbox {
    flex-grow: 1;
    overflow-y: auto;
}

:deep(.p-listbox-list-wrapper) {
    height: 100%;
}

.card {
    display: flex;
    flex-direction: column;
}
</style>