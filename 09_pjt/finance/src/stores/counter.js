import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios"

export const useVideoStore = defineStore('video', () => {
  const videos = ref([])
  const laters = ref([])
  const channels = ref([])

  const importVideos = function (inputData) {
    videos.value = []

    axios({
      method: 'get',
      url: 'https://www.googleapis.com/youtube/v3/search',
      params: {
        key: import.meta.env.VITE_API_KEY,
        part: 'snippet',
        type: 'videos',
        q: inputData,
        maxResults: 50,
        type: 'video',
      }
    })
    .then(res => {
      videos.value.push(...res.data.items)
    })
    .catch(err => console.error(err))
  }

  const addLaters = function(video) {
    laters.value.push(video)
    console.log('saved')
  }

  const deleteLaters = function(id) {
    const idx = laters.value.findIndex(video => video.id.videoId === id)
    laters.value.splice(idx, 1)
  }

  const addChannel = function(channelTitle) {
    channels.value.push(channelTitle)
    console.log('saved')
  }

  const deleteChannel = function(channelTitle) {
    const title = channels.value.findIndex(channel => channel === channelTitle)
    channels.value.splice(title, 1)
  }

  return { videos, laters, channels, importVideos, addLaters, deleteLaters, addChannel, deleteChannel }
}, { persist:true })
