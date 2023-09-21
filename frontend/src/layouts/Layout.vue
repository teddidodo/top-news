<template>
    <q-layout class="bg-grey-1">
      <q-header class="text-white" style="background: #24295e" height-hint="61.59">
        <q-toolbar class="q-mr-md">
          <q-btn class="q-my-md q-mr-md" round to="/">
            <q-avatar size="42px">
              <img src="https://png.pngtree.com/png-vector/20190826/ourlarge/pngtree-speaker-png-image_1696336.jpg">
            </q-avatar>
          </q-btn>
  
          <!-- <div v-if="$q.screen.gt.sm"
            class="GL__toolbar-link q-ml-xs q-gutter-md text-body2 text-weight-bold row items-center no-wrap">
            <a href="/news/profile/a?tab=" class="text-white">
              Saved News
            </a>
  
          </div> -->
  
          <q-space />
  
          <!-- <div class="q-pl-sm q-gutter-sm row items-center no-wrap">
  
            <q-btn dense flat no-wrap>
              <q-avatar rounded size="20px">
                DT
              </q-avatar>
              <q-icon name="arrow_drop_down" size="16px" />
  
              <q-menu auto-close>
                <q-list dense>
                  <q-item clickable class="GL__menu-link"><q-item-section>Help</q-item-section></q-item>
                  <q-item clickable class="GL__menu-link"><q-item-section>Settings</q-item-section></q-item>
                  <q-item clickable class="GL__menu-link">
                    <q-item-section>Log out</q-item-section>
                  </q-item>
                </q-list>
              </q-menu>
            </q-btn>
          </div> -->
        </q-toolbar>
      </q-header>
  
      <q-page-container>
        <!-- <LoadingScreen v-if="loading"></LoadingScreen> -->
        <router-view></router-view>
      </q-page-container>
    </q-layout>
  </template>
  
  <script>
  import { ref } from 'vue'
  import { fabGithub } from '@quasar/extras/fontawesome-v6'
  // import LoadingScreen from '@/views/LoadingScreen.vue'
  

  
  export default {
    name: 'MyLayout',
    components: {
      // LoadingScreen
    },

    // mounted() {
    //   setTimeout(() => {
    //     this.loading = false;
    //   }, 3000);
    // },
  
    setup() {
      const text = ref('')
      const search = ref(null) // $refs.search
      const loading = ref(true)
  
      return {
        fabGithub,
  
        text,
        search,
        loading
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