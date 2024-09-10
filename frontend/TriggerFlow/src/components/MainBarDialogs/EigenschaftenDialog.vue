<template>
  <Dialog :visible="visible" @update:visible="$emit('update:visible', $event)" :modal="true" :header="'Eigenschaften'" class="w-3/5 max-w-3xl">
    <div class="flex flex-col h-[550px] bg-gradient-to-br from-gray-900 to-gray-800 text-white p-6">
      <div class="flex-1 grid grid-cols-2 gap-4">
        <div class="col-span-2">
          <label for="name" class="block mb-1 text-lg">Name:</label>
          <InputText id="name" v-model="name" class="w-full bg-gray-700 text-white p-2 text-base" />
        </div>
        <div class="col-span-2">
          <label for="description" class="block mb-1 text-lg">Beschreibung:</label>
          <Textarea id="description" v-model="description" rows="4" class="w-full bg-gray-700 text-white p-2 text-base" />
        </div>
        <div>
          <label for="user" class="block mb-1 text-lg">Nutzer:</label>
          <InputText id="user" v-model="user" class="w-full bg-gray-700 text-white p-2 text-base" />
        </div>
        <div>
          <label for="creationDate" class="block mb-1 text-lg">Erstellungsdatum:</label>
          <InputText id="creationDate" :value="creationDate" class="w-full bg-gray-700 text-white p-2 text-base"
                     disabled/>
        </div>
      </div>
      <div class="flex justify-end mt-6">
        <Button label="Speichern" icon="pi pi-check" @click="saveProperties"
                class="bg-green-500 hover:bg-green-600 px-5 py-2 text-base"/>
      </div>
    </div>
  </Dialog>
</template>

<script setup>
import {ref, onMounted} from 'vue';
import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';

const props = defineProps({
  visible: Boolean
});

const emit = defineEmits(['update:visible']);

const name = ref('');
const description = ref('');
const user = ref('');
const creationDate = ref('');

onMounted(() => {
  creationDate.value = new Date().toLocaleDateString();
});

const saveProperties = () => {
  console.log('Saving properties:', {
    name: name.value,
    description: description.value,
    user: user.value,
    creationDate: creationDate.value
  });
  emit('update:visible', false);
};
</script>

<style scoped>
:deep(.p-dialog-content) {
  padding: 0 !important;
}

:deep(.p-inputtext) {
  background-color: #374151;
  color: white;
  border-color: #4B5563;
}

:deep(.p-button) {
  background-color: #10B981;
  border-color: #10B981;
}

:deep(.p-button:hover) {
  background-color: #059669;
  border-color: #059669;
}

:deep(.p-dialog-header) {
  padding: 1.5rem 1.5rem 1rem 1.5rem;
  background-color: #1F2937;
  color: white;
  font-size: 1.25rem;
}

:deep(.p-dialog-header-close) {
  color: white;
}
</style>