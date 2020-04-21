import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/signup',
    name: 'Signup',
    component: () => import('../views/Signup.vue')
  },
  {
    path: '/signup2',
    name: 'Signup2',
    component: () => import('../views/Signup2.vue')
  },
  {
    path: '/subarchive',
    name: 'SubArchive',
    component: () => import('../views/SubArchive.vue')
  },
  {
    path: '/manualscan',
    name: 'ManualScan',
    component: () => import('../views/ManualScan.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
