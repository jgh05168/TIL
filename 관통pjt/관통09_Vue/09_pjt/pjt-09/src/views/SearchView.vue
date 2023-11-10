<template>
    <div class="container">
        <div>
            <p>뒤로가기</p>
        </div>
        <h1>비디오 검색</h1>
        <form @submit.prevent="onSubmit" action="" @submit="getSearchData" class="input-group mb-3">
            <input type="text" class="form-control" placeholder="검색어를 입력해주세요" aria-label="Recipient's username" aria-describedby="button-addon2" v-model="searchVal">
            <button class="btn btn-success btn-outline-secondary text-white" type="submit" id="button-addon2">찾기</button>
        </form>

        <!-- card -->
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">
            <div class="col" v-for="video in videos">
                <router-link :to="video.id.videoId" class="card">
                    <img :src="video.snippet.thumbnails.high.url" class="card-img-top" alt="...">
                    <div class="card-body">
                        <p class="card-text">{{video.snippet.title }}</p>
                    </div>
                </router-link>
            </div>
        
 
        </div> 

    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const videos = ref([])
const searchData = ref('')
const searchVal = ref('')
const API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY

const getSearchData = function() {
    searchData.value = searchVal.value,
    searchVal.value = ''
    const storeURL = `https://www.googleapis.com/youtube/v3/search?key=${API_KEY}&type=video&part=snippet&q=${searchData.value}`
    
    axios.get(storeURL)
    .then ((response) => {
        videos.value = response.data.items
    }) 
    .catch ((error) => {
        console.error(error)
    })

}
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