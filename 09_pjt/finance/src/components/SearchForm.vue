<template>
  <div>
    <label for="search" class="form-label">
      <h2>비디오 검색</h2>
    </label>
    <form class="input-group mb-3">
      <input v-model="inputData" type="text" class="form-control" placeholder="검색어를 입력하세요" id="search">
      <button type="submit" class="btn btn-success" @click.prevent="store.importVideos(inputData)">찾기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useVideoStore } from '@/stores/counter'
const store = useVideoStore()

const inputData = ref('')
</script>

<style scoped>
</style>