<template>
  <nav class="navbar navbar-expand-sm bg-dark" data-bs-theme="dark">
    <div class="container-fluid">

      <RouterLink class="navbar-brand" :to="{ name: 'home' }">MyTube</RouterLink >

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-sm-0">
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'home' }">Home</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'search' }">Search</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'later' }">Later</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'subscribe' }">Channel</RouterLink>
          </li>
        </ul>
      </div>

    </div>
  </nav>
</template>

<script setup></script>

<style scoped></style>
