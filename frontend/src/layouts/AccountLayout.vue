<template>
  <q-layout class="bg-grey-1">
  

    <q-page-container style="padding-top: 10%; padding-left: 25%; padding-right: 25%">
      <!-- <q-card class="" > -->
        <router-view></router-view>
      <!-- </q-card> -->
      <!-- <div class="flex flex-center">Duc Thanh Do</div> -->
    </q-page-container>
  </q-layout>
</template>
  
  <script>
  // import { ref } from 'vue'
  // import LoadingScreen from '@/views/LoadingScreen.vue'


  import backgroundImage from '@/assets/background_account.jpg'
  
  export default {
    name: 'AccountLayout',
    components: {
      // LoadingScreen
    },

    mounted() {
      // setTimeout(() => {
      //   this.loading = false;
      // }, 3000);
    },
  
    setup() {
      return {
        backgroundImage
      }
    }
  }
  </script>
  
  <style lang="sass">
.GL
  &__select-GL__menu-link
    .default-type
      visibility: hidden

    &:hover
      background: #0366d6
      color: white
      .q-item__section--side
        color: white
      .default-type
        visibility: visible

  &__toolbar-link
    a
      color: white
      text-decoration: none
      &:hover
        opacity: 0.7

  &__menu-link:hover
    background: #0366d6
    color: white

  &__menu-link-signed-in,
  &__menu-link-status
    &:hover
      & > div
        background: white !important

  &__menu-link-status
    color: $blue-grey-6
    &:hover
      color: $light-blue-9

  &__toolbar-select.q-field--focused
    width: 450px !important
    .q-field__append
      display: none
</style>