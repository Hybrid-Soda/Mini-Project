<template>
  <div class="back-button">
    <button @click="goBack" class="btn">← 뒤로가기</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
function goBack() {
  router.go(-1)
}
</script>

<style scoped>
.back-button {
  margin-bottom: 20px;
}
</style>