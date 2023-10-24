import axios from 'axios';

const HTTP = axios.create({
  baseURL: process.env.NODE_ENV === 'production' ? process.env.VUE_APP_API : process.env.VUE_APP_API,
  headers: {}
});

export const requestAPI = async (promise) => {
    const result = await promise
    const data = result.data
    return data
}

export default HTTP;