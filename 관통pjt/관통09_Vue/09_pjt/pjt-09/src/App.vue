<template>
  <nav class="navbar bg-dark border-bottom border-body" data-bs-theme="dark">
  <div class="container-fluid">
    <RouterLink :to="{ name:'home' }" class="navbar-brand">MyTube</RouterLink>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <RouterLink :to="{name: 'home'}" class="nav-link">Home</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{name: 'search'}" class="nav-link">Search</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{name: 'later'}" class="nav-link">Later</RouterLink>
        </li>        
      </ul>
    </div>
  </div>
</nav>
<RouterView />
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'


</script>


<style scoped>

</style>