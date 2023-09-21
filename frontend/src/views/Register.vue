<template>
  <div>
    <div class="q-pa-md">
      <h2 class="text-h6 q-mb-md">Register an Account</h2>
      <q-form @submit="register">
        <div class="text-caption q-my-sm">Email</div>
        <q-input v-model="formData.email" outlined dense error-message="Please enter a valid email address" :error="!validateEmail" lazy-rules @change="validateEmailActivities"/>
        <div class="text-caption q-my-sm">Password</div>
        <q-input v-model="formData.password" outlined dense type="password" error-message="At least 9 characters with A to Z, a to z, special character, 0 to 9" @change="validatePasswordActivities" :error="!validatePassword" />
        <div class="text-caption q-my-sm">Repeat Password</div>
        <q-input v-model="formData.repeatPassword" type="password" outlined dense error-message="The repeat password should be the same as the password" :error="!validateRepeatPassword" @change="validateRepeatPasswordActivities"/>
        <q-btn type="submit" label="Register" color="primary" class="q-my-md"/>
        <br>
        <a class="" href="/login">Already have an account?</a>
      </q-form>
    </div>
  </div>
</template>
  
<script>
import { ref } from 'vue'
import {validateEmailMethod, validatePasswordMethod, validateRepeatPasswordMethod} from '@/utils/validation'


import {registerUserAPI} from '@/apis/users_api'

export default {
  name: 'MyRegister',

  setup() {
    const validateEmail = ref(true)
    const validatePassword = ref(true)
    const validateRepeatPassword = ref(true)
    const formData = ref({
      email: '',
      password: '',
      repeatPassword: ''
    })
    return {
      formData,
      registerUserAPI,
      validateEmail,
      validatePassword,
      validateRepeatPassword,
      validateEmailMethod, 
      validatePasswordMethod, 
      validateRepeatPasswordMethod
    };
  },
  methods: {
    async register() {

      if (this.validateEmail 
          && this.validatePassword 
          && this.validateRepeatPassword 
          && this.formData.email !== '' 
          && this.formData.password !== '' 
          && this.formData.repeatPassword !== '') {

        console.log('OK')
        await this.registerUserAPI(this.formData.email, this.formData.password)
        this.$router.push('/login');
      } else {
        console.log(process.env.API)
        console.log('Not OK')
      }
    },

    validateEmailActivities() {
      this.validateEmail = this.validateEmailMethod(this.formData.email)
    },
    validatePasswordActivities() {
      this.validatePassword = this.validatePasswordMethod(this.formData.password)
    },
    validateRepeatPasswordActivities() {
        this.validateRepeatPassword = validateRepeatPasswordMethod(this.formData.password, this.formData.repeatPassword)
    }    
  },
};
</script>
  