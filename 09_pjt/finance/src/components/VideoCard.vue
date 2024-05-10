<template>
  <div class="card">
    <img :src="video.snippet.thumbnails.high.url" class="card-img-top" alt="thumbnail">
    <div class="card-body">
      <p class="card-text">{{ video.snippet.title }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  video: Object
})
</script>

<style scoped>
.card {
  height: 100%;
}
</style>