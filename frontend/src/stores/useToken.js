import { defineStore } from 'pinia';
export const useToken = defineStore({
    id: 'authentication',
    state: () => ({
        token: localStorage.getItem('user_session')
    }),
    getters: {},
    actions: {
        setToken(token) {
            localStorage.setItem('user_session', token)
            this.token = token
        },
        getToken() {
            return this.token
        },
        getAuthorizationHeader() {
            return {
                'Authorization' : 'Bearer ' + localStorage.getItem('user_session'),
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        }
    }
})