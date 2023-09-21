import {
    createRouter,
    createWebHistory
} from "vue-router";
import routes from "./routes";

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach(async (to, from, next) => {
    console.log(to, from)
    const token = localStorage.getItem('user_session')
    if(token === null) {
        next('/login')
    }
    const timestamp = JSON.parse(window.atob(token.split('.')[1])).expires // Your timestamp
    const currentTimestamp = Date.now() / 1000; // Convert milliseconds to seconds

    if (to.path !== '/login' && to.path !== '/register' && timestamp <= currentTimestamp) {
        console.log("The provided timestamp is in the past.");
        next('/login')
    }
    console.log("The provided timestamp is equal to the current timestamp.");
    next()
})

export default router;
