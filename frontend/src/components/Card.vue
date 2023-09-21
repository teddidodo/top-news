<template>
  <q-card class="q-ma-md q-pa-md full-width" flat bordered>

    <q-card-section>
      <div class="text-h5 q-mt-sm q-mb-xs">{{ news?.title }} </div>
      <div class="text-overline text-orange-9">Published: {{ news?.pubDate ? news.pubDate : news.published }}</div>
      <div class="text-caption text-grey">
        {{ news?.description }}
      </div>
    </q-card-section>

    <q-card-actions>


      <!-- <q-btn :loading="loading[3]" flat @click="saveNews">
        {{ buttonText }}
        <template v-slot:loading>
          <q-spinner-hourglass class="on-left" />
          Loading...
        </template>
      </q-btn> -->
      <a :href="news?.link" class="" style="text-decoration: none">
        <q-btn flat>Views</q-btn>
      </a>

      <q-space />

      <q-btn color="grey" round flat dense :icon="expanded ? 'keyboard_arrow_up' : 'keyboard_arrow_down'"
        @click="expanded = !expanded" />
    </q-card-actions>

    <q-slide-transition>
      <div v-show="expanded">
        <q-separator />
        <q-card-section class="text-subtitle2">
          <text-caption>Sources</text-caption>
          <li>Category: {{ news?.category !== null ? news?.category.join(',') : '' }}</li>
          <!-- <li>Author: {{ news?.creator !== null ? news?.creator.join(',') : '' }}</li> -->
          <li>Keywords: {{ news?.keywords !== null ? news?.keywords.join(',') : '' }}</li>
          <li>Country: {{ news?.country !== null ? news?.country.join(',') : '' }}</li>
          <li>Source: {{ news?.source_id }}</li>
          <li>Language: {{ news?.language }}</li>
        </q-card-section>
      </div>
    </q-slide-transition>
  </q-card>
</template>
  
<script>
import { ref } from 'vue'

import { postNewsAPI, deleteQueryAPI } from '../apis/news_api'

export default {
  name: 'NewsCard',
  props: ['news'],


  methods: {
    async saveNews() {
      this.simulateProgress(3)
      console.log(this.news)
      const news = {
        title: this.news.title ? this.news.title : '',
        pubDate: this.news.pubDate ? this.news.pubDate : '',
        link: this.news.link ? this.news.link : '',
        description: this.news.description ? this.news.description : '',
        creator: this.news.creator ? this.news.creator : [],
        source_id: this.news.source_id ? this.news.source_id : '',
        country: this.news.country ? this.news.country : [],
        category: this.news.category ? this.news.category : [],
        language: this.news.language ? this.news.language : '',
        keywords: this.news.keywords ? this.news.keywords : [],
        query: 'python'
      }
      await postNewsAPI(news)

      this.buttonText = 'Saved'
    }
  },
  setup() {
    const loading = ref([
      false,
      false,
      false,
      false,
      false,
      false
    ])

    const buttonText = ref('Save')

    const progress = ref(false)

    function simulateProgress(number) {
      // we set loading state
      loading.value[number] = true

      // simulate a delay
      setTimeout(() => {
        // we're done, we reset loading state
        loading.value[number] = false
      }, 3000)
    }
    return {
      expanded: ref(false),
      lorem: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      loading,
      progress,
      simulateProgress,
      buttonText,
      deleteQueryAPI
    }
  }
}
</script>
  
<style lang="sass" scoped>
  .my-card
    width: 100%
    max-width: 350px
  </style>
  