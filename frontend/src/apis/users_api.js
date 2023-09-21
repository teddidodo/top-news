import HTTP, {requestAPI} from './http_common'
import {return_authorization_header} from '@/utils/token'

export const readUser = async (email) => {
    try {
      const readUserPromise = HTTP.get("/users/" + email, {headers: return_authorization_header()})
      const data = await requestAPI(readUserPromise)
      return data
      
    } catch (error) {
      console.log(error);
      return error
    }
}

export const registerUserAPI = async (email, password) => {
  try {
    const registerUserPromise = HTTP.post('/register', { email, password }, { headers: return_authorization_header() })
    await requestAPI(registerUserPromise)
  } catch (error) {
    console.log(error);
  }
}