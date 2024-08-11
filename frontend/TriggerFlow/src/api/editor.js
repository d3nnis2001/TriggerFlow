import axios from "axios";

export const runCode = async function runCode(
  code,
  lineCount,
  tableName,
  colName,
) {
  try {
    const cred = new URLSearchParams();
    cred.append("code", code);
    cred.append("linecount", lineCount);
    cred.append("tableName", tableName);
    cred.append("colName", colName);
    return await axios.post("/api/editor/runCode", cred);
  } catch (error) {
    console.error("Unseen error when sending code:", error);
    return false;
  }
};

export const refreshOutputCells = async function refreshOutputCells(
  code,
  lineCount,
  currCol,
) {
  try {
    const cred = new URLSearchParams();
    cred.append("code", code);
    cred.append("linecount", lineCount);
    cred.append("currCol", currCol);
    return await axios.post("/api/editor/refreshCode", cred);
  } catch (error) {
    console.error("Unseen error when getting refreshed output:", error);
    return false;
  }
};

export const saveCodeSnippet = async function saveCodeSnippet(name, code) {
  try {
    const cred = new URLSearchParams();
    cred.append("name", name);
    cred.append("code", code);
    return await axios.post("/api/editor/saveCodeSnippet", cred);
  } catch (error) {
    console.error("Unseen error when saving code snippet:", error);
    return false;
  }
};

export const getCodeSnippets = async function getCodeSnippets() {
  try {
    const response = await axios.get("/api/editor/getCodeSnippets");
    return response.data;
  } catch (error) {
    console.error("Unseen error when getting code snippets:", error);
    return false;
  }
};
