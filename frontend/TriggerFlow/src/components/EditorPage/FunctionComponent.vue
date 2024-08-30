<template>
  <div class="p-4 bg-gray-100 rounded-lg shadow-md flex items-center">
    <Button icon="pi pi-trash" class="p-button-danger p-button-rounded" @click="$emit('delete')" />
    <div class="ml-4 flex-grow">
      <h3 class="text-lg font-bold mb-2">{{ name }}</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <InputText v-for="(value, index) in inputValues" 
                   :key="index" 
                   v-model="inputValues[index]" 
                   :placeholder="`Input ${index + 1}`"
                   class="w-full" />
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
  inputCount: {
    type: Number,
    default: 2,
    validator: (value) => value >= 1 && value <= 5
  }
});

const emit = defineEmits(['delete', 'update:inputValues']);

const inputValues = ref(Array(props.inputCount).fill(''));

watch(() => props.inputCount, (newCount) => {
  inputValues.value = inputValues.value.slice(0, newCount).concat(Array(Math.max(0, newCount - inputValues.value.length)).fill(''));
});

watch(inputValues, (newValues) => {
  emit('update:inputValues', newValues);
}, { deep: true });
</script>

<style scoped>
/* Zusätzliche Stile können hier hinzugefügt werden */
</style>