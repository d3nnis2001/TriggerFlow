<template>
  <div class="bg-gray-800 rounded-lg shadow-lg overflow-hidden transition duration-300 ease-in-out hover:bg-gray-700">
    <div class="flex">
      <img :src="job.image" :alt="job.name" class="w-32 h-32 object-cover" />
      <div class="p-4 flex-grow">
        <h3 class="text-xl font-semibold text-white mb-2">{{ job.name }}</h3>
        <p class="text-gray-400 mb-2">{{ job.description }}</p>
        <p class="text-sm text-gray-500 mb-4">{{ formatDate(job.date) }}</p>
        <div class="flex space-x-2">
          <button
            @click="$emit('load', job)"
            class="bg-blue-600 hover:bg-blue-700 text-white text-sm font-bold py-1 px-3 rounded transition duration-300 ease-in-out"
          >
            Load Job
          </button>
          <button
            @click="$emit('edit', job)"
            class="bg-green-600 hover:bg-green-700 text-white text-sm font-bold py-1 px-3 rounded transition duration-300 ease-in-out"
          >
            Edit
          </button>
          <button
            @click="$emit('delete', job)"
            class="bg-red-600 hover:bg-red-700 text-white text-sm font-bold py-1 px-3 rounded transition duration-300 ease-in-out"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps(['job']);
defineEmits(['load', 'edit', 'delete']);

const formatDate = (date) => {
  return new Date(date).toLocaleDateString();
};
</script>