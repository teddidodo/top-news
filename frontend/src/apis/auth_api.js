import HTTP, {requestAPI} from './http_common'
import {setNewToken} from '@/utils/token'

export const loginAPI = async (email, password) => {
    try {
      const loginPromise = HTTP.post("/login", { email, password })
      const data = await requestAPI(loginPromise)
      setNewToken(data.access_token)
      localStorage.setItem('user_session', data.access_token)
    } catch (error) {
      console.log(error);
    }
}