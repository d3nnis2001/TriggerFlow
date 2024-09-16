import axios from "axios";

export const getGlobalVariables = async function(jobId) {
    try {
        const response = await axios.get(`/api/global-variables/${jobId}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching global variables:", error);
        throw error;
    }
};

export const createGlobalVariable = async function(jobId, variableData) {
    try {
        const response = await axios.post(`/api/global-variables/${jobId}`, {
            variable_data:  JSON.stringify(variableData),
        });
        return response.data;
    } catch (error) {
        console.error("Error creating global variable:", error);
        throw error;
    }
};

export const updateGlobalVariable = async function(jobId, variableData) {
    try {
        const response = await axios.put(`/api/global-variables/${jobId}`, {
            variable_data: JSON.stringify(variableData),
        });
        return response.data;
    } catch (error) {
        console.error("Error updating global variable:", error);
        throw error;
    }
};

export const checkExistance = async function(jobId) {
    try {
        const response = await axios.get(`/api/global-variables/exist/${jobId}`)
        console.log(response)
        return response.data
    } catch (error) {
        console.error("Error checking for global variables:", error);
        throw error;
    }
}