<template>
  <q-layout class="bg-grey-1">
    <q-page-container class="flex flex-center">
      <q-btn class="q-my-md q-mr-md" round>
        <q-avatar size="200px">
          <img src="https://png.pngtree.com/png-vector/20190826/ourlarge/pngtree-speaker-png-image_1696336.jpg">
        </q-avatar>
      </q-btn>
    </q-page-container>
    <q-page-container style="padding-top: 2%; padding-left: 15%; padding-right: 15%" class="row">
      <q-input square borderless dense use-input hide-selected class="col-10 shadow-1 q-pl-sm" v-model="text"
        style="max-width: 800px" hide-dropdown-icon>
      </q-input>
      <q-btn square class="col-2 bg-indigo-6 text-white shadow-2" dense @click="search">Search</q-btn>
    </q-page-container>
    <div class="flex flex-center" style="padding-top: 5%">Created by @Duc Thanh Do</div>
  </q-layout>
</template>
    
<script>
import { ref } from 'vue'
import backgroundImage from '@/assets/background_account.jpg'
import { postQueryAPI } from '@/apis/news_api'

export default {
  name: 'MyHome',
  components: {
  },
  methods: {
    async search() {
      await postQueryAPI(this.text)
      this.$router.push('/news?query=' + this.text)
    }
  },

  mounted() {
  },

  setup() {
    const text = ref('a')
    
    return {
      backgroundImage,
      text
    }
  }
}
</script>
    
<style lang="sass">
  </style>