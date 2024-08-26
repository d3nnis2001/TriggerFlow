import axios from "axios";
import { useToast } from "primevue/usetoast";
const toast = useToast();

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
export const uploadFiles = async function (formData) {
  try {
    const response = await axios.post("/api/nodes/uploadFiles", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    if (response.status === 200) {
      toast.add({
        severity: "success",
        summary: "Erfolg",
        detail: "Dateien erfolgreich hochgeladen",
        life: 3000,
      });
    } else {
      throw new Error("Upload fehlgeschlagen");
    }
  } catch (error) {
    console.error("Fehler beim Hochladen:", error);
    toast.add({
      severity: "error",
      summary: "Fehler",
      detail: "Dateien konnten nicht hochgeladen werden",
      life: 3000,
    });
  }
};
