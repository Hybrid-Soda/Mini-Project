<template>
  <div>
    <BackButton />
    <SearchForm />
    <div class="row g-3">
      <div class="col-sm-6 col-md-4 col-lg-3" v-for="video in store.videos" :key="video.etag">
        <RouterLink :to="{ name: 'detail', params: {'id':video.etag} }" class="button">
          <VideoCard :video="video" />
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import BackButton from '@/components/BackButton.vue'
import SearchForm from '@/components/SearchForm.vue'
import VideoCard from '@/components/VideoCard.vue'
import { useVideoStore } from '@/stores/counter'

const store = useVideoStore()
</script>

<style scoped>
.button {
  text-decoration: none;
}
</style>