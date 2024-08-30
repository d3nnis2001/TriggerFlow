import axios from "axios";

export const getFilereader = async function (
  filename,
  handler,
  firstRowHeading,
  from,
  till,
) {
  try {
    const url = new URL("/api/nodes/filereader", window.location.origin);
    url.searchParams.append("filename", filename);
    url.searchParams.append("handler", handler);
    url.searchParams.append("firstRowHeading", firstRowHeading);
    url.searchParams.append("from", from);
    url.searchParams.append("till", till);

    const response = await axios.get(url.toString());

    return response.data;
  } catch (error) {
    console.error("Fehler beim Holen der Datei:", error);
    throw error;
  }
};
export const uploadFiles = async function (formData) {
  try {
    const response = await axios.post("/api/nodes/uploadFiles", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    if (response.status === 200) {
      console.log("Hat alles funktioniert");
    } else {
      throw new Error("Upload fehlgeschlagen");
    }
  } catch (error) {
    console.error("Fehler beim Hochladen:", error);
  }
};
