import axios from 'axios';


export const runCode = async function runCode(code, lineCount) {
    try {
        const cred = new URLSearchParams()
        cred.append("code", code)
        cred.append("linecount", lineCount)
        return await axios.post("/api/editor/runCode", cred)
    } catch (error) {
        console.error("Unseen error when sending code:", error);
        return false
    }
}

export const refreshOutputCells = async function refreshOutputCells(code, lineCount, currCol) {
    try {
        const cred = new URLSearchParams()
        cred.append("code", code)
        cred.append("linecount", lineCount)
        cred.append("currCol", currCol)
        return await axios.post("/api/editor/refreshCode", cred)
    } catch (error) {
        console.error("Unseen error when getting refreshed output:", error);
        return false
    }
}