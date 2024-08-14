import axios from "axios";

export const uploadFile = async function (file) {
  try {
    const formData = new FormData();
    formData.append("file", file);

    return await axios.post("/api/nodes/fileupload", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
  } catch (error) {
    console.error("Fehler beim Hochladen der Datei:", error);
    throw error;
  }
};

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
