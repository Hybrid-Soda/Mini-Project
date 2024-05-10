<template>
  <div>
    <BackButton />
    <h2>나중에 볼 동영상</h2>
    <div v-if="store.laters.length" class="row g-3">
      <div class="col-sm-6 col-md-4 col-lg-3" v-for="video in store.laters">
        <RouterLink :to="{ name: 'detail', params: {'id': video.etag} }">
          <VideoCard :video="video" />
        </RouterLink>
      </div>
    </div>
    <p v-else>등록된 비디오 없음</p>
  </div>
</template>

<script setup>
import BackButton from '@/components/BackButton.vue'
import VideoCard from '@/components/VideoCard.vue'
import { useVideoStore } from '@/stores/counter';
const store = useVideoStore()

</script>

<style scoped>

</style>