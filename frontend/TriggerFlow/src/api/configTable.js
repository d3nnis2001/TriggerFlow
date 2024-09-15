import axios from "axios";

// Create a new config table
export const createTable = async function createTable(table_id, jobId, tableName, tableData) {
    try {
        const payload = {
            job_id: jobId,
            table_name: tableName,
            table_data: JSON.stringify(tableData)
        };

        return await axios.post(`/api/config-tables/${table_id}`, payload);
    } catch (error) {
        console.error("Error when creating table:", error);
        return false;
    }
};

// Get all tables by job ID
export const getAllTablesByJob = async function getAllTablesByJob(jobId) {
    try {
        return await axios.get(`/api/config-tables/job/${jobId}`);
    } catch (error) {
        console.error("Error when fetching tables for job:", error);
        return false;
    }
};

// Get a specific table by table ID
export const getTable = async function getTable(tableId) {
    try {
        return await axios.get(`/api/config-tables/${tableId}`);
    } catch (error) {
        console.error("Error when fetching table:", error);
        return false;
    }
};

// Update a table by table ID
export const updateTable = async function updateTable(tableId, jobId, tableName, tableData) {
    try {
        const payload = {
            job_id: jobId,
            table_name: tableName,
            table_data: tableData
        };
        return await axios.put(`/api/config-tables/${tableId}`, payload);
    } catch (error) {
        console.error("Error when updating table:", error);
        return false;
    }
};

// Delete a table by table ID
export const deleteTableBack = async function deleteTableBack(tableId) {
    try {
        return await axios.delete(`/api/config-tables/${tableId}`);
    } catch (error) {
        console.error("Error when deleting table:", error);
        return false;
    }
};
