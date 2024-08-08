import {
  TextInputInterface,
  ButtonInterface,
} from "@baklavajs/renderer-vue";

import {
  defineNode,
  NodeInterface,
} from "@baklavajs/core";

// Hilfsfunktion zum Erstellen des File-Input-Elements und Auswählen einer Datei
function createFileInput(callback) {
  const input = document.createElement("input");
  input.type = "file";
  input.style.display = "none";
  input.onchange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        callback(file.name, e.target.result);
      };
      reader.readAsText(file);
    }
  };
  document.body.appendChild(input);
  input.click();
  document.body.removeChild(input);
}

// Definiere die FileReader Node
export const FileReader = defineNode({
  type: "FileReader",
  title: "File Reader",
  inputs: {
    path: () => new TextInputInterface("File Path", "").setPort(false),
    selectFile: () => new ButtonInterface("Select File").setPort(false),
  },
  outputs: {
    to_next: () => new NodeInterface("To next", null),
  },
  data: {
    fileContent: null,
  },
  calculate(inputs) {
    if (inputs.path) {
      const fileContent =
        this.data.fileContent || readFileFromPath(inputs.path);
      return {
        to_next: fileContent,
      };
    }
    return {
      to_next: null,
    };
  },
  created() {
    this.inputs.selectFile.on("click", () => {
      createFileInput((fileName, fileContent) => {
        this.inputs.path.value = fileName;
        this.data.fileContent = fileContent;
        this.calculate(this.inputs);
      });
    });
  },
});

function readFileFromPath(path) {
  // Hier könnte eine Logik zum Lesen der Datei basierend auf dem Pfad implementiert werden.
  // Zum Beispiel:
  return `Mock content for the file at ${path}`;
}
