<template>
    <div class="card flex justify-center">
        <Listbox v-model="selectedCode" :options="codeSnippets" optionLabel="name" filter class="w-full h-full">
            <template #option="slotProps">
                <div class="flex items-center">
                    <div v-tooltip.left="{ value: slotProps.option.description, showDelay: 1000, hideDelay: 200 }">{{ slotProps.option.name }}</div>
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

const selectedCode = ref();
</script>

<style scoped>
.p-listbox {
    height: 100%;
}
</style>