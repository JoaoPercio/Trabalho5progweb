<template>
  <biblioteca-navbar>
    <template #right>
      <div class="d-flex align-items--center">
        <biblioteca-button class="aa" @click="onLivros">
          Jogos
        </biblioteca-button>
        <biblioteca-button class="aa" @click="onEmprestimos">
          salas
        </biblioteca-button>
        <biblioteca-button class="aa" @click="onUsuarios">
          Usuários
        </biblioteca-button>
        <biblioteca-button class="aa" @click="onLogout">
          Sair
        </biblioteca-button>
      </div>
    </template>
  </biblioteca-navbar>
</template>

<script>
import { removeCookie } from '@/helpers/cookies/cookie';
import { goToLoginPage } from '@/router/route.service';
import { goToLivros, goToEmprestimos, goToUsuarios } from '@/modules/gerenciar/gerenciar.routes';

export default {
  name: 'BibliotecaTopbar',
  data() {
    return {
    };
  },
  methods: {
    removeCookie,
    onLogout() {
      removeCookie('session_id');
      goToLoginPage();
    },
    onLivros() {
      goToLivros(this.$router);
    },
    onEmprestimos() {
      goToEmprestimos(this.$router);
    },
    onUsuarios() {
      goToUsuarios(this.$router);
    },
  },
};
</script>
<style>
 .aa{
  background-color: #6404FF !important;
  border: none !important;
  color:aliceblue;
  font-weight: 600;
  font-size: 1000px;
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
 }
</style>
