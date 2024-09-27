import axios from "axios";

export const getAllJobs = async function getAllJobs() {
  try {
    console.log("Auführen allgetjob");
    const response = await axios.get("/api/joblist/getAllJobs");
    return response.data;
  } catch (error) {
    console.error("Unseen error when getting Jobs:", error);
    return false;
  }
};  


export const createNewJob = async function createNewJob (name, description, date, comp, image) {
  try {
    const response = await axios.post("/api/joblist/createJob", {
      name: name, 
      description: description, 
      date: date,
      comp: comp,
      image: image,
    });
    return response.data;
  } catch (error) {
    console.log("Error when creating a new job:", error)
    throw error;
  }
}