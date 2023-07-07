import axios from 'axios';

const BASE_URL = 'http://6c0f-41-90-180-222.ngrok-free.app';

export const loginUser = async (email, password) => {
  try {
    const response = await axios.post(`${BASE_URL}/user/signup`, { email, password });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};


// http://127.0.0.1:5555

// 