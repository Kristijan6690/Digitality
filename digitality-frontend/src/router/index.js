import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Croppa from 'vue-croppa'
import Notifications from 'vue-notification'
import Loading from 'vue-loading-overlay';
import { Auth } from '@/services'

Vue.use(Loading, {
  color: '#00A2FF'
});
 
Vue.use(Notifications)

Vue.use(Croppa)  

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { requiresAuth: true }
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
    path: '/scan',
    name: 'Scan',
    component: () => import('../views/Scan.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/signup2',
    name: 'Signup2',
    component: () => import('../views/Signup2.vue')
  },
  {
    path: '/subarchive/:naziv_arhive',
    name: 'SubArchive',
    component: () => import('../views/SubArchive.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/subarchive.documentinfo/:id',
    name: 'SubArchive.DocumentInfo',
    component: () => import('../views/SubArchive.DocumentInfo.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/manualscan',
    name: 'ManualScan',
    component: () => import('../views/ManualScan.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/editdocument/:id',
    name: 'EditDocument',
    component: () => import('../views/EditDocument.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/alias_list',
    name: 'AliasList',
    component: () => import('../views/AliasList.vue'),
    meta: { requiresAuth: true }
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


router.beforeEach( (to,from,next) => {
  if(to.matched.some(record => record.meta.requiresAuth)){
    if(localStorage.getItem('user')) {
      next();
    }
    else{
      router.replace('/login');
    }
  }
  else {
    next();
  }
});
export default router
