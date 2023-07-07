import axios from "axios";

const BASE_URL = "https://6c0f-41-90-180-222.ngrok-free.app";

export const loginUser = async (data) => {
  try {
    const response = await axios.post(`${BASE_URL}/user/login`, data);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// http://127.0.0.1:5555

//
