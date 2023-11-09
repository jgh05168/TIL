<template>
    <div>
        <h1>UserView</h1>
        <h2>{{ $route.params.id }}번 User 페이지</h2>
        <h2>{{ userId }}번 User 페이지</h2>
        <button @click="goHome">홈으로!</button>
        <button @click="goAnotherUser">100번 유저 페이지로!</button>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router';

    const route = useRoute()
    const userId = ref(route.params.id)

    const router = useRouter()
    const goHome = function () {
        router.push({name: 'home'})
    }

    //in-component Guard
    // 1. onBeforeRouteLeave
    onBeforeRouteLeave((to, from) => {
        const ans = window.confirm('정말 떠나실 건가요?')       //return값이 존재함

        if (ans === false) {
            return false
        }
    })

    //2. onBeforeRouteUpdate
    const goAnotherUser = function () {
        router.push({name: 'user', params: {id: 100}})
    }

    onBeforeRouteUpdate ((to, from) => {
        console.log(to)
        userId.value = to.params.id
    })
</script>

<style scoped>

</style>