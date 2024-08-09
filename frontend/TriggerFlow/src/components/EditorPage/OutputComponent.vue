<template>
    <div ref="outputContainer" class="output-container">
        <div class="output-scroll">
            <div
                v-for="(output, index) in outputs"
                :key="index"
                class="output-cell"
            >
                {{ output }}
            </div>
        </div>
    </div>
</template>

<script>
import { ref, watch, onMounted } from "vue";

export default {
    name: "OutputComponent",
    props: {
        outputs: Array,
        editorScrollTop: Number,
    },
    setup(props) {
        const outputContainer = ref(null);
        const lineHeight = 1.4; // em

        const updateScroll = () => {
            if (outputContainer.value) {
                const containerHeight = outputContainer.value.clientHeight;
                const scrollHeight = props.outputs.length * (lineHeight * 16);
                outputContainer.value.style.overflowY =
                    scrollHeight > containerHeight ? "scroll" : "hidden";
            }
        };

        watch(
            () => props.editorScrollTop,
            (newScrollTop) => {
                if (outputContainer.value) {
                    outputContainer.value.scrollTop = newScrollTop;
                }
            },
        );

        watch(() => props.outputs.length, updateScroll);

        onMounted(updateScroll);

        return { outputContainer };
    },
};
</script>

<style scoped>
.output-container {
    width: 200px;
    border-left: 1px solid #ddd;
    overflow-y: hidden;
    margin-top: 0.2em;
}
.output-scroll {
    height: 100%;
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
