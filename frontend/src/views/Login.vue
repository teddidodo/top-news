<template>
    <div>
        <div class="q-pa-md">
            <h2 class="text-h6 q-mb-md">Login to Your Account</h2>
            <q-form @submit="login">
                <div class="text-caption q-my-sm">Email</div>
                <q-input v-model="formData.email" outlined dense @input="clearError" />
                <div class="text-caption q-my-sm">Password</div>
                <q-input v-model="formData.password" type="password" outlined dense @input="clearError" />
                <q-btn type="submit" label="Login" color="primary" class="q-my-md" />
                <br>
                <a class="q-my-md text-overline" href="/register">Don't have an account yet!</a>
                <q-alert v-if="error" color="negative" icon="warning" :options="{ dense: true }">
                    {{ error }}
                </q-alert>
            </q-form>
        </div>
    </div>
</template>
  
<script>
import { ref } from 'vue'
import { loginAPI } from '@/apis/auth_api'

export default {
    name: 'MyLogin',
    setup() {
        const formData = ref({
            email: '',
            password: ''
        })

        const error = ref('')

        return {
            formData,
            error,
            loginAPI
        };
    },
    methods: {
        async login() {
            await this.loginAPI(this.formData.email, this.formData.password)
            this.$router.push('/')
            // this.$router.push('/search');
            // Successful login, navigate to another page (e.g., dashboard)
            // this.$router.push('/dashboard');
        },
        clearError() {
            this.error = '';
        },
    },
};
</script>
  