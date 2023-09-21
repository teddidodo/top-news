import axios from 'axios';

const HTTP = axios.create({
  baseURL: process.env.NODE_ENV === 'production' ? process.env.API : process.env.API,
  headers: {}
});

export const requestAPI = async (promise) => {
    const result = await promise
    const data = result.data
    return data
}

export default HTTP;