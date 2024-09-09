<!-- TableDialog.vue -->
<template>
  <Dialog :visible="visible" @update:visible="$emit('update:visible', $event)" modal header="Tabelle" :style="{ width: '50vw' }">
    <p>Hier können Sie den Inhalt Ihrer Tabelle einfügen.</p>
    <!-- Add your table content here -->
  </Dialog>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';
import Dialog from 'primevue/dialog';

const props = defineProps({
  visible: Boolean
});

const emit = defineEmits(['update:visible']);

// You can add more logic here if needed
</script>