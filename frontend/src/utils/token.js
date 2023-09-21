import {useToken} from '@/stores/useToken'
// import {storeToRefs} from 'pinia'

const currentToken = useToken()

export const getCurrentToken = () => {
    return currentToken.getToken()
} 

export const setNewToken = (token) => {
    return currentToken.setToken(token)
}

export const return_authorization_header = () => {
    return currentToken.getAuthorizationHeader()
}
