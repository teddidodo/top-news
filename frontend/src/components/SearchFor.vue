<template>
  <div class="text-h5 flex flex-center q-mt-md">Searching For: '{{ query }}'</div>
</template>

<style>
</style>

<script>
export default {
  name: 'SearchFor',
  props: [
    'query'
  ]
}
</script>
