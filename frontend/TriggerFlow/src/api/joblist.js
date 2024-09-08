import axios from "axios";

export const getAllJobs = async function getAllJobs() {
  try {
    console.log("Auführen allgetjob");
    const response = await axios.post("/api/joblist/getAllJobs");
    return response.data;
  } catch (error) {
    console.error("Unseen error when getting Jobs:", error);
    return false;
  }
};  
