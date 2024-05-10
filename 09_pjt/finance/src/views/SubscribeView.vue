<template>
  <div>
    <BackButton />
    <h2 class="mb-4">저장한 채널 목록</h2>
    <div v-for="channel in store.channels">
      <p>{{ channel }}</p>
    </div>
  </div>
</template>

<script setup>
import BackButton from '@/components/BackButton.vue'
import { useVideoStore } from '@/stores/counter'

const store = useVideoStore()

</script>

<style scoped>

</style>