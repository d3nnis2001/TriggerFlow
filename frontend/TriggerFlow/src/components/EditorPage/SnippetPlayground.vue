  <template>
    <div class="recktangle" @dragover.prevent @drop="onDrop">
      <div class="flex-grow overflow-y-auto p-3">
        <draggable class="dragArea list-group w-full" :list="functions" @change="log">
          <div
            class="list-group-item bg-gray-300 m-1 p-3 rounded-md"
            v-for="(func, index) in functions"
            :key="`${func.name}-${index}`"
          >
            <FunctionComponent :name="func.name" :params="func.params" @delete="deleteFunction(index)"/>
          </div>
        </draggable>
      </div>
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
        functions: [],
        dragging: false,
      }
    },
    methods: {
      log(event) {
        console.log(event)
      },
      onDrop(event) {
        const droppedFunction = JSON.parse(event.dataTransfer.getData('text/plain'));
        const newFunction = {
          ...droppedFunction,
          id: `${droppedFunction.name}-${Date.now()}`
        };
        this.functions.push(newFunction);
      },
      deleteFunction(index) {
        this.functions.splice(index, 1);
      }
    },
  })
  </script>

  <style>
  .recktangle {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
  }

  .list-group-item {
    cursor: move;
  }
  </style>