<template>
    <div class="flex flex-col h-screen">
        <div class="flex flex-row w-screen">
            <div class="w-5/6">
                <div v-for="item in fsatz">
                    <MapFunction :propData="item" />
                </div>
            </div>
            <div class="w-1/6 h-full">
                <Listbox v-model="selectedMapping" :options="mapping" optionLabel="name" :highlightOnSelect="false" class="h-full" />
            </div>
        </div>
        <TableComponent/>
    </div>
</template>

<script setup>
import { ref } from "vue";
import Listbox from 'primevue/listbox';
import MapFunction from "../components/Mapping/MapFunction.vue";
import TableComponent from "../components/EditorPage/TableComponent.vue"

const selectedMapping = ref();

const mapping = ref([
    { name: 'F-Satz'},
    { name: 'G-Satz'},
    { name: 'K-Satz'},
    { name: 'S-Satz'},
    { name: 'A-Satz'},
    { name: 'F-Satz'},
    { name: 'G-Satz'},
    { name: 'K-Satz'},
    { name: 'S-Satz'},
    { name: 'A-Satz'}
]);

const fsatz = ref([
    { name :'Datum', fixedValue :'', needed:true },
    { name :'Belegnummer',  fixedValue :'', needed:true },
    { name :'Interne Belegnummer', fixedValue :'', needed:false },
    { name :'Externe Belegnummer', fixedValue :'', needed:true },
    { name :'Betrag', fixedValue :'', needed:true },
    { name :'Währung', fixedValue :'', needed:true },
]);

</script>

<style scoped>
</style>
