<template>
  <div class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4">
    <div class="bg-gray-800 rounded-lg shadow-xl p-6 w-full max-w-md">
      <h3 class="text-2xl font-bold text-white mb-4">Neuen Job erstellen</h3>
      <form @submit.prevent="createJob">
        <div class="mb-4">
          <label for="jobName" class="block text-sm font-medium text-gray-400 mb-1">Job Name</label>
          <input
            id="jobName"
            v-model="newJob.name"
            type="text"
            required
            class="w-full px-3 py-2 bg-gray-700 text-white rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <div class="mb-4">
          <label for="jobDescription" class="block text-sm font-medium text-gray-400 mb-1">Beschreibung</label>
          <textarea
            id="jobDescription"
            v-model="newJob.description"
            required
            rows="3"
            class="w-full px-3 py-2 bg-gray-700 text-white rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          ></textarea>
        </div>
        <div class="flex justify-end space-x-3">
          <button
            type="button"
            @click="$emit('close')"
            class="px-4 py-2 bg-gray-600 text-white rounded-md hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500"
          >
            Abbrechen
          </button>
          <button
            type="submit"
            class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            Erstellen
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { defineEmits } from 'vue';

const emit = defineEmits(['close', 'create']);

const newJob = ref({
  name: '',
  description: '',
  company: '',
  image: '',
});

const createJob = () => {
  emit('create', { ...newJob.value });
};

</script>