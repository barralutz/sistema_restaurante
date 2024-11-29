// src/router/index.js
import Vue from 'vue';
import VueRouter from 'vue-router';
import LoginView from '@/views/Login.vue';
import CrearPedidoView from '@/views/CrearPedido.vue';
import PedidosMeseroView from '@/views/PedidosMesero.vue';
import PartesAreaView from '@/views/PartesArea.vue';
import CajaView from '@/views/Caja.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/mesero/crear-pedido',
    name: 'CrearPedido',
    component: CrearPedidoView,
  },
  {
    path: '/mesero/pedidos',
    name: 'PedidosMesero',
    component: PedidosMeseroView,
  },
  {
    path: '/area/:area',
    name: 'PartesArea',
    component: PartesAreaView,
  },
  {
    path: '/caja',
    name: 'Caja',
    component: CajaView,
  },
  // Otras rutas
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

// Guardias de navegación
router.beforeEach((to, from, next) => {
  const publicPages = ['/login'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('accessToken');

  if (authRequired && !loggedIn) {
    return next('/login');
  }

  next();
});

export default router;
