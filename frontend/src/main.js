import { createApp } from 'vue'
import App from './App.vue'
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import router from './routes/router'
import { createPinia } from 'pinia'

createApp(App).use(Quasar, quasarUserOptions).use(createPinia()).use(router).mount('#app')
