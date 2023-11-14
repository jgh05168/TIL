<template>
  <div>
    <h1>DETAIL</h1>
    <p>ID: {{ article.id }}</p>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
  </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/article'
import axios from 'axios'
import { onMounted } from 'vue'
import { useRoute } from 'vue-router';
import { ref } from 'vue';

const store = useArticleStore()
const route = useRoute()
const article = ref({})

onMounted(()=> {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}`
  })
  .then((response) => {
    // console.log(response.data)
    article.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })
})

</script>

<style>

</style>
