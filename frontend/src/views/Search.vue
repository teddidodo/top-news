<template>
    <div>
        <SearchFor />
        <div class="row">
          <NewsCard v-for="x in 4" :key="x" class="col" />
        </div>
    </div>
</template>

  <script>
//   import { ref } from 'vue'  
  import NewsCard from '../components/Card.vue'
  import SearchFor from '../components/SearchFor.vue'
  
  export default {
    name: 'MyHome',
  
    components: {
      SearchFor,
      NewsCard
    },
  
    setup() {
  
      return {
      }
    }
  }
  </script>