<template>
    <div class="container">
            <div>
                <p>뒤로가기</p>
            </div>
            <h1>나중에 볼 동영상</h1>
            
            <div v-if="laterVideos" class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">
                <div class="col" v-for="video in laterVideos">
                    <router-link :to="video.id" class="card">
                        <img :src="video.snippet.thumbnails.high.url" class="card-img-top" alt="...">
                        <div class="card-body">
                            <p class="card-text">{{video.snippet.title }}</p>
                        </div>
                    </router-link>
                </div>
            </div>
            <div v-else>
                <p style="opacity: 0.5;">등록된 비디오 없음</p>
            </div>
        </div>
    </template>
    
    <script setup>
    import { ref, computed } from 'vue'
    import { useRouter } from 'vue-router'
    import axios from 'axios'
    
    const router = useRouter()
    const laterVideos = ref('')
    
    laterVideos.value = JSON.parse(localStorage.getItem('video')) || []
    console.log(laterVideos.value)
    
    
    </script>
    
    <style scoped>
    .card {
    width: 100%; /* 카드 전체 폭을 100%로 설정 */
    height: 100%; /* 카드 전체 높이를 100%로 설정 */
    }

    .card-img-top {
    width: 100%; /* 이미지 폭을 100%로 설정 */
    height: auto; /* 이미지 높이를 자동으로 조정 */
}
    </style>