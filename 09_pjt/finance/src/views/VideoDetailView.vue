<template>
  <div>
    <BackButton />
    <h1>{{ video.snippet.title }}</h1>
    <p>업로드 날짜: {{ video.snippet.publishTime.split('T')[0] }}</p>
    <iframe
      :src=videoUrl
      :title="video.snippet.title"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen
    ></iframe>
    <p>{{ description }}</p>
    <button v-if="!isSaved(video.id.videoId)" @click="store.addLaters(video)" class="btn btn-primary">동영상 저장</button>
    <button v-if="isSaved(video.id.videoId)" @click="store.deleteLaters(video.id.videoId)" class="btn btn-secondary">동영상 저장 취소</button>
  
    <button v-if="!isChannelSaved(channelTitle)" @click="store.addChannel(channelTitle)" class="btn btn-warning ms-2">채널 저장</button>
    <button v-if="isChannelSaved(channelTitle)" @click="store.deleteChannel(channelTitle)" class="btn btn-warning ms-2">채널 저장 취소</button>
  </div>
</template>

<script setup>
import BackButton from '@/components/BackButton.vue'
import { useVideoStore } from '@/stores/counter'
import { useRoute } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from "axios"

const route = useRoute()
const store = useVideoStore()
const etag = ref(route.params.id)
const video = ref(store.videos.find((video => video.etag == etag.value)))
const videoUrl = `https://www.youtube.com/embed/${video.value.id.videoId}`
const description = ref('')
const channelTitle = ref(video.value.snippet.channelTitle)

onMounted (() => {
  axios({
    method: 'get',
    url: 'https://www.googleapis.com/youtube/v3/videos',
    params: {
      key: import.meta.env.VITE_API_KEY,
      part: 'snippet',
      id: video.value.id.videoId,
    }
  }).then(res => {
    description.value = res.data.items[0].snippet.description
  }).catch(error => {
    console.error(error)
  })
})

const isSaved = function(id) {
  console.log(store.laters)
  if (store.laters.find(video => video.id.videoId === id)) {
    return true
  } else {
    return false
  }
}

const isChannelSaved = function(channelTitle) {
  if (store.channels.find(channel => channel === channelTitle)) {
    console.log(channelTitle)
    return true
  } else {
    return false
  }
}
</script>

<style scoped>
iframe {
  width: 90%;
  height: 480px;
}
</style>