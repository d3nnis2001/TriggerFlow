<template>
    <div class="editor-wrapper">
        <div ref="editorElement" class="editor"></div>
    </div>
</template>

<script>
import { onMounted, ref } from "vue";
import { EditorView, keymap, lineNumbers } from "@codemirror/view";
import { EditorState } from "@codemirror/state";
import { basicSetup } from "codemirror";
import { python } from "@codemirror/lang-python";
import { autocompletion } from "@codemirror/autocomplete";
import { indentWithTab } from "@codemirror/commands";

export default {
    name: "EditorComponent",
    emits: ["update:modelValue", "scroll"],
    props: {
        modelValue: String,
    },
    setup(props, { emit }) {
        const editorElement = ref(null);
        let editorView;

        onMounted(() => {
            const editorState = EditorState.create({
                doc: props.modelValue,
                extensions: [
                    basicSetup,
                    lineNumbers(),
                    python(),
                    autocompletion(),
                    keymap.of([indentWithTab]),
                    EditorView.lineWrapping,
                    EditorState.tabSize.of(4),
                    EditorView.updateListener.of((update) => {
                        if (update.docChanged) {
                            emit(
                                "update:modelValue",
                                update.state.doc.toString(),
                            );
                        }
                    }),
                ],
            });

            editorView = new EditorView({
                state: editorState,
                parent: editorElement.value,
            });

            editorElement.value.addEventListener("scroll", () => {
                emit("scroll", editorElement.value.scrollTop);
            });
        });

        return { editorElement };
    },
};
</script>

<style scoped>
.editor-wrapper {
    flex: 1;
    overflow: hidden;
}
.editor {
    height: 100%;
    overflow-y: auto;
    font-family: "Fira Code", monospace;
    font-size: 14px;
}
</style>
