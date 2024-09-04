<template>
  <div :class="containerClass" class="flex flex-row border-2 border-white items-center rounded-xl mb-2 p-2">
    <InputText id="fixedval" size="large" placeholder="Fix Wert" v-model="fixedval" class="text-white flex-1" />
    <Select v-model="valueChoose" :options="columns" optionLabel="name" placeholder="Wähle Spalte" class="w-full md:w-56 flex-1" />
    <p class="text-white text-xl flex-1">{{ propData?.name || 'No name available' }}</p>
  </div>
</template>

<script setup>
import { defineProps, ref, computed } from 'vue';
import InputText from 'primevue/inputtext';
import Select from 'primevue/select';

const fixedval = ref("");
const valueChoose = ref("");
const columns = [{name: "Belegart"}, {name: "Währung"}, {name: "Belegnummer"}, {name: "Betrag Netto"}];

const props = defineProps({
  propData: {
    type: Object,
    required: true
  }
});

const containerClass = computed(() => {
  if (props.propData.needed) {
    if (fixedval.value || valueChoose.value) {
      return 'bg-green-200';
    } else {
      return 'bg-red-200'; 
    }
  }
  return ''; 
});

</script>

<style scoped>
.bg-green-200 {
  background-color: #c6f6d5;
}

.bg-red-200 {
  background-color: #feb2b2;
}
</style>
