<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
    <div class="container">
      <nav>
        <RouterLink to="/">Home</RouterLink> | 
        <RouterLink to="/detail">상세페이지 테스트용</RouterLink> | 
        <RouterLink to="cart">장바구니</RouterLink>
      </nav>

  <RouterView />
    </div>

</template>


<style scoped>
.container {
  width: 90%;
  margin: 0 auto;
}
</style>
