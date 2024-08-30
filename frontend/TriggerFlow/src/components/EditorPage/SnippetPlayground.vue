<template>
  <div class="recktangle">
    <draggable class="dragArea list-group w-full" :list="functions" @change="log">
      <div
        class="list-group-item bg-gray-300 m-1 p-3 rounded-md"
        v-for="func in functions"
        :key="func.name"
      >
        <h3 class="font-bold text-lg mb-2">{{ func.name }}</h3>
        <p class="text-sm text-gray-600">{{ func.description }}</p>
        <FunctionComponent :name="func.name" :params="func.params"/>
      </div>
    </draggable>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import { VueDraggableNext } from 'vue-draggable-next'
import FunctionComponent from './FunctionComponent.vue'

export default defineComponent({
  components: {
    draggable: VueDraggableNext,
    FunctionComponent,
  },
  data() {
    return {
      enabled: true,
      functions: [
        { 
          name: 'calculateSum', 
          description: 'Berechnet die Summe zweier Zahlen',
          params: ['a', 'b']
        },
        { 
          name: 'formatDate', 
          description: 'Formatiert ein Datum',
          params: ['date', 'format']
        },
        { 
          name: 'filterArray', 
          description: 'Filtert ein Array basierend auf einer Bedingung',
          params: ['array', 'condition']
        },
        { 
          name: 'sendEmail', 
          description: 'Sendet eine E-Mail',
          params: ['to', 'subject', 'body']
        },
      ],
      dragging: false,
    }
  },
  methods: {
    log(event) {
      console.log(event)
    },
  },
})
</script>

<style>
.recktangle {
  display: flex;
  flex-direction: column;
  width: 85vw;
  height: 100%;   
  border: solid white 2px;
}

.list-group-item {
  cursor: move;
}
</style>