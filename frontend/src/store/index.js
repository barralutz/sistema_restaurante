// src/store/index.js
import Vue from 'vue';
import Vuex from 'vuex';
import router from '../router';
import apiClient from '../services/api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    accessToken: localStorage.getItem('accessToken') || '',
    refreshToken: localStorage.getItem('refreshToken') || '',
    user: null,
  },
  mutations: {
    setAccessToken(state, token) {
      state.accessToken = token;
    },
    setRefreshToken(state, token) {
      state.refreshToken = token;
    },
    setUser(state, user) {
      state.user = user;
    },
    logout(state) {
      state.accessToken = '';
      state.refreshToken = '';
      state.user = null;
    },
  },
  actions: {
    login({ commit }, credentials) {
      return apiClient.post('token/', credentials).then((response) => {
        commit('setAccessToken', response.data.access);
        commit('setRefreshToken', response.data.refresh);
        localStorage.setItem('accessToken', response.data.access);
        localStorage.setItem('refreshToken', response.data.refresh);
        // Obtener información del usuario
        return apiClient.get('user/').then((res) => {
          commit('setUser', res.data);
          router.push('/');
        });
      });
    },
    logout({ commit }) {
      commit('logout');
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      router.push('/login');
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.accessToken,
    getUser: (state) => state.user,
  },
  modules: {},
});
