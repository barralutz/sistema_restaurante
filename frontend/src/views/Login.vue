<!-- src/views/Login.vue -->
<template>
  <div class="login">
    <h1>Iniciar Sesión</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">Usuario:</label>
        <input type="text" v-model="username" required />
      </div>
      <div>
        <label for="password">Contraseña:</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">Ingresar</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    ...mapActions(['login']),
    login() {
      this.login({ username: this.username, password: this.password })
        .then(() => {
          this.$router.push('/');
        })
        .catch(() => {
          alert('Credenciales incorrectas');
        });
    },
  },
};
</script>

<style scoped>
/* Estilos para el componente */
</style>
