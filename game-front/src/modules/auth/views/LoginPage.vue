<template>
  <div class="row">
    <div class="col">
      <img src="@/assets/images/a.png" height="100%" width="100%">
    </div>
    <div class="col">
      <div class="container-sm">
        <biblioteca-container class="d-flex justify-content-center align-items-center h-100 py--xl">
          <biblioteca-form v-slot="{ validate }" :submit="submitLogin">
            <div class="text-center mb-3">
              <biblioteca-header size="sm" class="titulo">Login</biblioteca-header>
            </div>
            <div class="mb-3">
              <biblioteca-input
                v-model="email"
                type="email"
                name="e-mail"
                rules="required|email"
                placeholder="E-mail"
                :focus="true" />
            </div>
            <div class="mb-3">
              <biblioteca-input
                v-model="senha"
                name="senha"
                type="password"
                rules="required|min:6"
                placeholder="Senha" />
            </div>
            <div class="d-grid mb-3">
              <biblioteca-button
                class="btn btn-primary"
                native-type="submit"
                @click="validate">
                Entrar
              </biblioteca-button>
            </div>
            <div class="d-grid text-center">
              <p>
                Não possui conta?
                <router-link class="color--primary" to="/registrar">Criar conta</router-link>
              </p>
            </div>
          </biblioteca-form>
        </biblioteca-container>
      </div>
    </div>
  </div>
</template>

<script>
import * as authStore from '@/modules/auth/auth.store';
import { toastError } from '@/services/toastService';
import { passwordLogin } from '@/modules/auth/auth.service';
import { goToBasePage } from '@/router/route.service';

export default {
  name: 'BibliotecaLoginPage',
  data() {
    return {
      email: '',
      senha: '',
    };
  },
  beforeCreate() {
    if (authStore.getters.getToken()) {
      goToBasePage();
    }
  },
  methods: {
    submitLogin() {
      passwordLogin(this.email, this.senha)
        .then(goToBasePage)
        .catch(err => {
          if (err.response.data.detail === 'USUARIO_INCORRETO') {
            toastError('E-mail e/ou senha incorretos');
          }
        });
    },
  },
};
</script>
<style scoped>
   html,
    body {
        height: 100%;
    }

    .row {
        height: 100%;
    }

    .col {
        display: flex;
    }
span {
  width: 320px;
}
button {
  background-color: #6404FF;
  border: none !important;
}
button:hover{
  background-color: #6404FF !important;
}
.container-sm{
  box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25) !important;
  border-radius: 5px !important;
  margin: 3% 6% 2% 3%;
}
.titulo{
  color:#6404FF;
  font-size: 40px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
</style>
