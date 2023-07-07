import axios from 'axios';

const BASE_URL = 'http://localhost:5555'; // Replace with your actual backend URL

export const loginUser = async (email, password) => {
  try {
    const response = await axios.post(`${BASE_URL}/user/login`, { email, password });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};
