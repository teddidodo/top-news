import { createApp } from 'vue'
import App from './App.vue'
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import router from './routes/router'
import { createPinia } from 'pinia'

import { inject } from '@vercel/analytics';
 
inject();

createApp(App).use(Quasar, quasarUserOptions).use(createPinia()).use(router).mount('#app')
