import axios from "axios";
export const checkLoginData = async function checkLoginData(email, password) {
  try {
    const cred = new URLSearchParams();
    cred.append("email", email);
    cred.append("password", password);
    return await axios.post("/api/login/checkLogin", cred);
  } catch (error) {
    console.error("Unseen error when logging in:", error);
    return false;
  }
};
