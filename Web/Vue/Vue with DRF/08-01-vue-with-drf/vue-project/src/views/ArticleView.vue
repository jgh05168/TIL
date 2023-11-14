<template>
  <div>
    <h1>Article page</h1>
    <RouterLink :to="{name: 'CreateView'}">[CREATE]</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import ArticleList from '@/components/ArticleList.vue'
import { RouterLink } from 'vue-router'
import { useArticleStore } from '@/stores/article.js'

const store = useArticleStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style>

</style>
