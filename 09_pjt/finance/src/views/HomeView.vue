<template>
  <div class="home position-absolute top-50 start-50 translate-middle">
    <h1 class="home-title">MYTUBE</h1>
    <p>보고싶은 동영상을 검색해보세요!</p>
    <RouterLink :to="{ name: 'search' }">
      <button class="btn btn-primary">검색하러가기</button>
    </RouterLink>
  </div>
</template>

<script setup>
</script>

<style scoped>
.home {
  text-align: center;
}

.home-title {
  margin-bottom: 20px;
  font-weight: 900;
}
</style>