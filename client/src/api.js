import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:5555';

export const loginUser = async (email, password) => {
  try {
    const response = await axios.post(`${BASE_URL}/user/login`, { email, password });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};
