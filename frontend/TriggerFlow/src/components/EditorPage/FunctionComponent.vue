<template>
  <div class="p-1 bg-gray-100 rounded-lg shadow-md flex items-center">
    <Button icon="pi pi-trash" class="p-button-danger p-button-rounded p-button-sm" @click="$emit('delete')" />
    <div class="ml-1 flex-grow">
      <h3 class="text-sm font-bold mb-0.5">{{ name }}</h3>
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-1">
        <InputText v-for="(param, index) in params" 
                   :key="index" 
                   v-model="inputValues[index]" 
                   :placeholder="param"
                   class="w-full text-white py-0.5 px-1 text-xs" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';

const props = defineProps({
  name: {
    type: String,
    required: true
  },
  params: {
    type: Array,
    default: () => []
  },
});

const emit = defineEmits(['delete', 'update:inputValues']);

const inputValues = ref(Array(props.params.length).fill(''));

watch(() => props.params.length, (newLength) => {
  inputValues.value = inputValues.value.slice(0, newLength).concat(Array(Math.max(0, newLength - inputValues.value.length)).fill(''));
});

watch(inputValues, (newValues) => {
  emit('update:inputValues', newValues);
}, { deep: true });
</script>

<style scoped>
</style>
