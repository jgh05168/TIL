<template>
    <div>
      {{ article.title }}
      <p>{{ article.content }}</p>
  </div>
  <RouterLink :to="{name: 'DetailView', params: {id: article.id}}">[DETAIL]</RouterLink>
  <hr>

</template>

<script setup>
import { RouterLink } from 'vue-router';
import DetailView from '@/views/DetailView.vue'

defineProps({
  article: Object,
})
</script>
