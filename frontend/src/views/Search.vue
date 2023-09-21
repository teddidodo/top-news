<template>
  <div>
    <div class="row q-ma-md flex flex-center">
      <q-input square borderless dense use-input hide-selected class="col-10 shadow-1 q-pl-md" v-model="text"
         hide-dropdown-icon>
      </q-input>
      <q-btn class="col-2 bg-indigo-6 text-white q-py-sm" dense square @click="search">Search</q-btn>
    </div>
    <SearchFor class="q-ma-md" :query="query" />
    <div class="row">
      <NewsCard v-for="x in news" :key="x.id" :news="x"/>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import NewsCard from '../components/Card.vue'
import SearchFor from '../components/SearchFor.vue'
import { readNews } from '../apis/news_api'

export default {
  name: 'MyHome',

  methods: {
    async search() {
      this.news = []
      this.query = this.text
      this.news = await readNews(this.text)
    }
  },

  components: {
    SearchFor,
    NewsCard
  },
  async mounted() {
    const urlParams = new URLSearchParams(window.location.search);
    this.query = urlParams.get('query');
    this.news = await readNews(this.query)
  },

  setup() {
    const query = ref('')
    const news = ref([])
    const text = ref('')
    return {
      query,
      readNews,
      news,
      text
    }
  }
}
</script>