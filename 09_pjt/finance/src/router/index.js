import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import VideoSearchView from '@/views/VideoSearchView.vue'
import VideoDetailView from '@/views/VideoDetailView.vue'
import LaterVideoView from '@/views/LaterVideoView.vue'
import SubscribeView from '@/views/SubscribeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/search/',
      name: 'search',
      component: VideoSearchView,
    },
    {
      path: '/search/:id',
      name: 'detail',
      component: VideoDetailView,
    },
    {
      path: '/later/',
      name: 'later',
      component: LaterVideoView
    },
    {
      path: '/subscribe/',
      name: 'subscribe',
      component: SubscribeView
    },
  ]
})

export default router
