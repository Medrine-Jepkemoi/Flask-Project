import axios from 'axios';

const BASE_URL = 'http://6c0f-41-90-180-222.ngrok-free.app'; // Replace with your actual backend URL

export const loginUser = async (email, password) => {
  try {
    const response = await axios.post(`${BASE_URL}/user/signup`, { email, password });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};


// http://localhost:5555
// http://6c0f-41-90-180-222.ngrok-free.app