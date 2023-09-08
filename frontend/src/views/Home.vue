<template>
  <q-layout class="bg-grey-1">
    <q-page-container class="flex flex-center" style="padding-top: 5%">
      <q-btn class="q-my-md q-mr-md" round>
        <q-avatar size="200px">
              <img src="https://png.pngtree.com/png-vector/20190826/ourlarge/pngtree-speaker-png-image_1696336.jpg">
            </q-avatar>
          </q-btn>
    </q-page-container>
    <q-page-container style="padding-top: 2%; padding-left: 15%; padding-right: 15%" class="row">
      <q-select ref="search" square borderless dense use-input hide-selected class="col-10 shadow-1 q-pl-sm"
       v-model="text" style="max-width: 800px" hide-dropdown-icon>
      </q-select>
      <q-btn square class="col-2 bg-indigo-6 text-white shadow-2" dense to="/news">Search</q-btn>
    </q-page-container>

    <div class="flex flex-center" style="padding-top: 5%">Created by @Duc Thanh Do</div>
  </q-layout>
</template>
    
<script>
// import { ref } from 'vue'
// import LoadingScreen from '@/views/LoadingScreen.vue'


import backgroundImage from '@/assets/background_account.jpg'

export default {
  name: 'MyHome',
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
  </style>