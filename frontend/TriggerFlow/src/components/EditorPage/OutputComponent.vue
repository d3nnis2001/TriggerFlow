<template>
    <div ref="outputContainer" class="output-container">
        <div
            v-for="(output, index) in outputs"
            :key="index"
            class="output-cell"
        >
            {{ output }}
        </div>
    </div>
</template>

<script>
import { ref, watch } from "vue";

export default {
    name: "OutputComponent",
    props: {
        outputs: Array,
        editorScrollTop: Number,
    },
    setup(props) {
        const outputContainer = ref(null);

        watch(
            () => props.editorScrollTop,
            (newScrollTop) => {
                if (outputContainer.value) {
                    outputContainer.value.scrollTop = newScrollTop;
                }
            },
        );

        return { outputContainer };
    },
};
</script>

<style scoped>
.output-container {
    width: 200px;
    border-left: 1px solid #ddd;
    overflow-y: scroll;
    display: flex;
    flex-direction: column;
}
.output-cell {
    height: 1.4em;
    line-height: 1.4em;
    padding: 0 5px;
    font-size: 14px;
    border-bottom: 1px solid #eee;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>
