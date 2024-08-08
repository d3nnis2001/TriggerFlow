<template>
  <vue-good-table
      :columns="columns"
      :rows="rows"
      :sort-options="{
      enabled: true
    }"
      :pagination-options="{
      enabled: true,
      perPage: 10
    }"
      :search-options="{
      enabled: true
    }"
      :filter-options="{
      enabled: true,
      filterByColumn: true
    }"
      :line-numbers="true"
      styleClass="vgt-table condensed"
  />
</template>

<script>
import { VueGoodTable } from 'vue-good-table-next';
import 'vue-good-table-next/dist/vue-good-table-next.css'

export default {
  components: {
    VueGoodTable
  },
  data() {
    return {
      columns: [
        {
          label: 'Header 1',
          field: 'col1',
          filterOptions: {
            enabled: true,
            placeholder: 'Filter Header 1'
          }
        },
        {
          label: 'Header 2',
          field: 'col2',
          filterOptions: {
            enabled: true,
            placeholder: 'Filter Header 2'
          }
        },
        // ... weitere Spalten
      ],
      rows: [
        { col1: 'Value 1', col2: 'Value 2' },
        // ... weitere Zeilen
      ]
    }
  }
}
</script>