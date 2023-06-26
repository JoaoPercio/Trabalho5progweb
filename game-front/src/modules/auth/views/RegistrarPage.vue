<template>
  <el-main>
    <div class="container">
      <biblioteca-row>
        <biblioteca-col
          class="text-center mb-3"
          :sm="12"
          :offset="6">
          <biblioteca-header size="md" class="titulo">Cadastro</biblioteca-header>
        </biblioteca-col>
      </biblioteca-row>
      <biblioteca-row>
        <biblioteca-col
          class="text-center mb-3"
          :sm="12"
          :offset="6">
          <biblioteca-form v-slot="{ validate }" :submit="validateUsuario">
            <biblioteca-row>
              <biblioteca-col
                class="text-center mb-3">
                <biblioteca-input
                  v-model="info.nome"
                  type="text"
                  name="nome"
                  rules="required"
                  placeholder="Nome"
                  :focus="true" />
              </biblioteca-col>
            </biblioteca-row>
            <biblioteca-row>
              <biblioteca-col
                class="text-center mb-3">
                <biblioteca-input
                  v-model="info.email"
                  type="email"
                  name="e-mail"
                  rules="required|email"
                  placeholder="E-mail" />
              </biblioteca-col>
            </biblioteca-row>
            <biblioteca-row>
              <biblioteca-col
                class="text-center mb-3">
                <biblioteca-input
                  v-model="info.senha"
                  name="senha"
                  type="password"
                  rules="required|min:6"
                  placeholder="Senha*" />
              </biblioteca-col>
            </biblioteca-row>
            <biblioteca-row>
              <biblioteca-col class="text-start">
                <input id="flexCheckDefault" v-model="idadeChecked" class="form-check-input" type="checkbox">
                <label class="form-check-label" for="flexCheckDefault"> Possuo mais de <strong style="color:#6404FF">18 anos de idade</strong></label>
              </biblioteca-col>
            </biblioteca-row>
            <biblioteca-row>
              <biblioteca-col class="text-start">
                <input id="flexCheckDefault" v-model="termosChecked" class="form-check-input" type="checkbox">
                <label class="form-check-label" for="flexCheckDefault"> Concordo com os <strong style="color:#6404FF">
                  <a href="https://dontpad.com/termosdeusodositedopettersonkkkk">termos de uso</a></strong></label>
              </biblioteca-col>
            </biblioteca-row>
            <biblioteca-row>
              <biblioteca-col
                class="text-center mb-3">
                <biblioteca-button
                  native-type="submit"
                  class="btn btn-dark"
                  @click="validate">
                  Cadastrar
                </biblioteca-button>
              </biblioteca-col>
            </biblioteca-row>
          </biblioteca-form>
        </biblioteca-col>
      </biblioteca-row>
      <biblioteca-row>
        <biblioteca-col
          class="text-center mb-3"
          :sm="12"
          :offset="6">
          <div class="d-grid text-center">
            <p>
              Já possui conta?
              <router-link class="color--primary" to="/login">Login</router-link>
            </p>
          </div>
        </biblioteca-col>
      </biblioteca-row>
    </div>
  </el-main>
</template>

<script>
import * as authStore from '@/modules/auth/auth.store';
import { registrar } from '@/modules/auth/auth.service';
import { toastError } from '@/services/toastService';
import { goToBasePage } from '@/router/route.service';

export default {
  name: 'BibliotecaRegistrarPage',
  provide() {
    const infoRegistrarVm = {};
    Object.defineProperty(infoRegistrarVm, 'info', {
      get: () => this.info,
    });
    return { infoRegistrarVm };
  },
  data() {
    return {
      info: {
        idadeChecked: false,
        termosChecked: false,
        nome: null,
        email: null,
        senha: null,
        confirmar_senha: null,
      },
    };
  },
  beforeCreate() {
    if (authStore.getters.getToken()) {
      goToBasePage();
    }
  },
  methods: {
    onRegistrar() {
      registrar(this.info)
        .then(goToBasePage)
        .catch(err => {
          if (err.response.data.detail === 'EMAIL_DUPLICADO') {
            toastError('E-mail duplicado');
          }
        });
    },
    validateUsuario() {
      if (this.idadeChecked && this.termosChecked) {
        this.onRegistrar();
      } else if (!this.idadeChecked) {
        toastError('Necessario ser maior de 18 anos para acessar nosso site');
      } else if (!this.termosChecked) {
        toastError('Necessario concordar com os termos de uso para acessar nosso site');
      }
    },
  },
};
</script>
<style scoped>
span {
  width: 620px;
}
button {
  width:150px;
  background-color:#6404FF ;
}.container{
  box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25) !important;
 border-radius: 20px !important;

}
.titulo{
  margin-top: 10% !important;
  color:#6404FF;
  font-size: 40px;
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
}
.text-start{
  text-align: left !important;
}
#flexCheckDefault{
  border-color:#6404FF !important;
}

</style>
