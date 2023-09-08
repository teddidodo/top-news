<template>
    <div>
        <div class="q-pa-md">
          <h2 class="text-h6 q-mb-md">Register an Account</h2>
          <q-form @submit="register">
            <div class="text-caption q-my-sm">Email</div>
            <q-input
              v-model="formData.email"
              outlined
              dense
              @input="clearError"
            />
            <div class="text-caption q-my-sm">Password</div>
            <q-input
              v-model="formData.password"
              outlined
              dense
              @input="clearError"
            />
            <div class="text-caption q-my-sm">Repeat Password</div>
            <q-input
              v-model="formData.repeatPassword"
              type="password"
              outlined
              dense
              @input="clearError"
            />
            <q-btn type="submit" label="Register" color="primary" class="q-my-md" />
            <br>
            <a class="" href="/account/login">Already have an account?</a>
            <q-alert
              v-if="error"
              color="negative"
              icon="warning"
              :options="{ dense: true }"
            >
              {{ error }}
            </q-alert>
        
          </q-form>
        </div>
    </div>
  </template>
  
  <script>
  import {ref} from 'vue'
  export default {
    name: 'MyRegister',

    setup() {
        const formData = ref({
            email: '',
            password: '',
            repeatPassword: ''
        })
        const error = ref('')
      return {
        formData,
        error
      };
    },
    methods: {
      register() {
        // Implement your registration logic here
        // For a basic example, you can display the user's input in an alert
        alert(`Name: ${this.formData.name}\nEmail: ${this.formData.email}`);
  
        // You can also navigate to another page after successful registration
        // this.$router.push('/login');
      },
      clearError() {
        this.error = '';
      },
    },
  };
  </script>
  