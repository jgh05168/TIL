<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <input type="text" v-model.trim="title">
      <textarea v-model.trim="content"></textarea>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/article'
import axios from 'axios';
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const store = useArticleStore()
const router = useRouter()

const title = ref('')
const content = ref('')

const createArticle = function() {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    }
  })
  .then((response) => {
    console.log(response)
    router.push({path:'/'})
  })
  .catch((error) => {
    console.log(error)
  })
}
</script>

<style>

</style>
