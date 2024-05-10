<template>
  <header>
    <NavigationBar />
  </header>

  <main class="main-container">
    <RouterView />
  </main>
</template>

<script setup>
import NavigationBar from '@/components/NavigationBar.vue'
</script>

<style scoped>
.main-container {
  margin: 30px 10% 0;
}
</style>