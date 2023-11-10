<template>
      <div class="container" v-if="video">
        <div>
            <p>뒤로가기</p>
        </div>
        <h1>{{ video.snippet.title }}</h1>
        <p>업로드 날짜:{{ video.publishedAt }}</p>

        <iframe width="100%" height="500" 
        :src="getVideoEmbedUrl(videoId)"
        frameborder="0"
        allowfullscreen></iframe>

        <p>{{ video.snippet.description}}</p>
        <div v-if="isSeen">
            <button  @click="addLaterVideo(video)" type="button" class="btn btn-primary">저장</button>
        </div>
        <div v-else>
            <button  @click="removeLaterVideo(video)" type="button" class="btn btn-primary">저장 취소</button>
        </div>
      </div>
      <div v-else>
        <p>로딩중</p>
      </div>
</template>



<script setup>
import { ref, watch } from 'vue'
import { useRoute , useRouter } from 'vue-router'
import axios from 'axios'
const router = useRouter()
const route = useRoute()
const videoId = ref(route.params.id)
const API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY
const storeURL = `https://www.googleapis.com/youtube/v3/videos?key=${API_KEY}&part=snippet&id=${videoId.value}`
const video = ref('')
const isSeen =ref(false)

axios.get(storeURL)
.then ((response) => {
    video.value = response.data.items[0]
    console.log(video.value)
    isSeen.value = isDuplicated(video.value)
}) 
.catch ((error) => {
    console.error(error)
})


const isDuplicated = function(video) {
    const existingVideo = JSON.parse(localStorage.getItem('video')) || []
    const find = existingVideo.length > 0 && existingVideo.find((item) => item.id === video.id)
    console.log(find)
    return !find }

const addLaterVideo = (video) => {
    const existingVideo = JSON.parse(localStorage.getItem('video')) || []

    const isDuplicate = existingVideo.length > 0 && existingVideo.find((item) => item.id === video.id)

    if (!isDuplicate) {
        existingVideo.push(video)
    }
    isSeen.value=false
    localStorage.setItem('video', JSON.stringify(existingVideo))

}

const removeLaterVideo = (video) => {
    const existingVideo = JSON.parse(localStorage.getItem('video')) || []

    const videoIdx = existingVideo.findIndex((item) => item.id === video.id)

    existingVideo.splice(videoIdx, 1)
    
    localStorage.setItem('video', JSON.stringify(existingVideo))
    isSeen.value=true
}

const getVideoEmbedUrl = function(videoId) {
  return `https://www.youtube.com/embed/${videoId}`;
};

</script>

<style scoped>

</style>