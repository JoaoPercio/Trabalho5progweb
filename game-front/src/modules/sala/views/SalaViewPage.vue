<template>
  <biblioteca-single-content-layout container-size="lg">
    <template v-if="emprestimo" #content>
      <div class="container">
        <biblioteca-row class="d-flex align-items-center">
          <biblioteca-col>
            <biblioteca-header class="titulo">
              {{ emprestimo.nome }}
            </biblioteca-header>
          </biblioteca-col>
        </biblioteca-row>
        <biblioteca-row class="mt-1">
          <biblioteca-col>
            <biblioteca-p class="biblioteca-u-text--medium">
              <biblioteca-usuario-link :id="emprestimo.usuario.id" target="_blank">
                <strong>Dono: </strong>{{ emprestimo.usuario.nome }}
              </biblioteca-usuario-link>
            </biblioteca-p>
          </biblioteca-col>
          <biblioteca-col>
            <biblioteca-p class="biblioteca-u-text--medium">
              <biblioteca-livro-link :id="emprestimo.jogo.id" target="_blank">
                <strong>Jogo: </strong>{{ emprestimo.jogo.nome }}
              </biblioteca-livro-link>
            </biblioteca-p>
          </biblioteca-col>
          <biblioteca-col>
            <biblioteca-p class="biblioteca-u-text--medium">
              <strong>descricao:</strong> {{ emprestimo.descricao }}
            </biblioteca-p>
          </biblioteca-col>
        </biblioteca-row>
        <biblioteca-row class="mt-1">
          <biblioteca-col>
            <biblioteca-p class="biblioteca-u-text--medium">
              <strong>Data: </strong>{{ formatarData(emprestimo.hora) }}
            </biblioteca-p>
          </biblioteca-col>
        </biblioteca-row>
      </div>
    </template>
  </biblioteca-single-content-layout>
</template>

<script>
import moment from 'moment';

import { EMPRESTIMO_ERRORS } from '@/modules/sala/sala.constants';
import { getEmprestimo } from '@/modules/sala/sala.service';
import { toastError } from '@/services/toastService';
// eslint-disable-next-line import/no-cycle
import { goToEmprestimoNotFound } from '@/modules/sala/sala.routes';
import BibliotecaSingleContentLayout from '@/layouts/SingleContentLayout.vue';
import BibliotecaUsuarioLink from '@/modules/usuario/components/UsuarioLink.vue';
import BibliotecaLivroLink from '@/modules/jogo/components/JogoLink.vue';

export default {
  name: 'EmprestimoViewPage',
  components: {
    BibliotecaUsuarioLink,
    BibliotecaLivroLink,
    BibliotecaSingleContentLayout,
  },
  data() {
    return {
      emprestimo: null,
    };
  },
  computed: {
    id() {
      return this.$route.params?.id;
    },
  },
  mounted() {
    this.fetch();
  },
  methods: {
    fetch() {
      getEmprestimo(this.id)
        .then(({ data }) => {
          this.emprestimo = data;
        })
        .catch(err => {
          this.emprestimo = null;
          if (err) {
            goToEmprestimoNotFound(this.$router);
          } else if ((err.response.data.errors === EMPRESTIMO_ERRORS[err.response.status] && err.response.status === 404)) {
            goToEmprestimoNotFound(this.$router);
          } else {
            toastError('Erro ao buscar a sala');
          }
        });
    },
    formatarData(data) {
      return moment(data).format('DD/MM/YYYY HH:mm');
    },
  },
};
</script>
<style>
.container{
  box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25) !important;
 border-radius: 20px !important;

}
.titulo{
  color: #5E0CE3 !important;
  text-align: center;
  font-family: 'Sigmar';
}
</style>
