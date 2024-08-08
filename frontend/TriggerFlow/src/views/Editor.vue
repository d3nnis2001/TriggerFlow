<template>
  <div class="main-container">
    <div class="top-buttons">
      <div class="play-button">
        <button @click="runCode">
          <i class="fas fa-play"></i>
        </button>
      </div>
      <div class="refresh-button">
        <button @click="refreshOutput">
          <i class="fas fa-sync-alt"></i>
        </button>
      </div>
    </div>
    <div class="top-section">
      <div class="editor-container">
        <div class="editor-wrapper">
          <div ref="editorElement" class="editor"></div>
        </div>
        <div class="output-cells">
          <div v-for="n in lineCount" :key="n" class="output-cell">
            <!-- Hier kommt später der Zwischenoutput -->
          </div>
        </div>
      </div>
      <div class="right-panels">
        <div class="panel docs">
          <h3>Docs / Funktionen</h3>
          <div class="scrollable-content">
            <div v-for="func in docsFunctions" :key="func.name" class="function-item">
              <strong>{{ func.name }}</strong>: {{ func.description }}
            </div>
          </div>
        </div>
        <div class="panel variables">
          <h3>Variables</h3>
          <div class="scrollable-content">
            <!-- Inhalt für Variablen hier -->
          </div>
        </div>
      </div>
    </div>
    <div class="bottom-section">
      <table-component></table-component>
    </div>
  </div>
</template>

<script>
import {onMounted, ref, reactive, computed} from 'vue'
import {EditorView, keymap, lineNumbers} from '@codemirror/view'
import {EditorState} from '@codemirror/state'
import {basicSetup} from 'codemirror'
import {python} from '@codemirror/lang-python'
import {autocompletion} from '@codemirror/autocomplete'
import {indentWithTab} from '@codemirror/commands'
import TableComponent from '../components/TableComponent.vue'

export default {
  components: {
    TableComponent
  },
  setup() {
    const editorElement = ref(null)
    const state = reactive({
      lineCount: 1
    })
    const docsFunctions = [
      { name: 'len(string)', description: 'Gibt die Länge eines Strings zurück.' },
      { name: 'str.upper()', description: 'Konvertiert einen String in Großbuchstaben.' },
      { name: 'str.lower()', description: 'Konvertiert einen String in Kleinbuchstaben.' },
      { name: 'str.strip()', description: 'Entfernt Leerzeichen am Anfang und Ende eines Strings.' },
      { name: 'int(string)', description: 'Konvertiert einen String in eine Ganzzahl.' },
      { name: 'float(string)', description: 'Konvertiert einen String in eine Fließkommazahl.' },
      { name: 'str.split(separator)', description: 'Teilt einen String an einem Separator in eine Liste.' },
      { name: 'str.join(iterable)', description: 'Verbindet Elemente einer Liste zu einem String.' },
      { name: 'str.replace(old, new)', description: 'Ersetzt Teile eines Strings.' },
      { name: 'abs(number)', description: 'Gibt den Absolutwert einer Zahl zurück.' },
    ]

    function runCode() {
      console.log('Führe Code aus');
    }

    function refreshOutput() {
      console.log('Aktualisiere Ausgabe');
    }

    onMounted(() => {
      const editorState = EditorState.create({
        extensions: [
          lineNumbers(),
          basicSetup,
          python(),
          autocompletion(),
          keymap.of([indentWithTab]),
          EditorView.lineWrapping,
          EditorState.tabSize.of(4),
          EditorView.updateListener.of(update => {
            if (update.docChanged) {
              state.lineCount = update.state.doc.lines
            }
          })
        ]
      })

      new EditorView({
        state: editorState,
        parent: editorElement.value
      })
    })

    return {
      editorElement,
      lineCount: computed(() => state.lineCount),
      docsFunctions,
      refreshOutput,
      runCode,
    }
  }
}
</script>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 80vw;
}

.top-section {
  display: flex;
  height: 65%;
}

.editor-container {
  display: flex;
  flex-grow: 1;
  border: 1px solid #ccc;
  border-radius: 4px;
  overflow: hidden;
  margin-right: 10px;
}

.line-numbers {
  width: 25px;
  background-color: #f7f7f7;
  border-right: 1px solid #ddd;
  overflow-y: hidden;
}

.line-number {
  text-align: right;
  padding: 0 5px;
  font-size: 14px;
  color: #999;
  height: 24px;
  line-height: 24px;
}

.editor-wrapper {
  flex-grow: 1;
  overflow: hidden;
}

.editor {
  height: 100%;
  overflow-y: auto;
  font-family: 'Fira Code', monospace;
  font-size: 14px;
}

.output-cells {
  width: 200px;
  border-left: 1px solid #ddd;
  overflow-y: hidden;
}

.output-cell {
  height: 24px;
  border-bottom: 1px solid #eee;
  padding: 0 5px;
  font-size: 14px;
  line-height: 24px;
}

.right-panels {
  width: 250px;
  display: flex;
  flex-direction: column;
}

.panel {
  flex: 1;
  border: 1px solid #ccc;
  border-radius: 4px;
  overflow: hidden;
  margin-bottom: 10px;
}

.panel h3 {
  margin: 0;
  padding: 10px;
  background-color: #f7f7f7;
  color: black;
  border-bottom: 1px solid #ddd;
}

.scrollable-content {
  height: calc(100% - 40px);
  overflow-y: auto;
  padding: 10px;
}

.bottom-section {
  height: 30%;
  overflow: auto;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-top: 10px;
}

.function-item {
  margin-bottom: 8px;
}

:deep(.cm-editor) {
  height: 100%;
}

:deep(.cm-scroller) {
  overflow: auto;
}

:deep(.cm-gutters) {
  display: none;
}

:deep(.cm-activeLine) {
  background-color: rgba(232, 242, 254, 0.3);
}

.top-buttons {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

.play-button,
.refresh-button {
  background-color: #f7f7f7;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 5px;
  cursor: pointer;
}

.play-button button,
.refresh-button button {
  background-color: transparent;
  border: none;
  color: #333;
  font-size: 16px;
}

</style>