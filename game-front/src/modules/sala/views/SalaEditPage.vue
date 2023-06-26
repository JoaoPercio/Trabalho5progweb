<template>
  <biblioteca-single-content-layout container-size="lg">
    <template #content>
      <div class="container">
        <biblioteca-header v-if="isEditing" class="titulo">
          Editar Sala
        </biblioteca-header>
        <biblioteca-header v-else class="titulo">
          Criar Sala
        </biblioteca-header>
        <biblioteca-emprestimo-edit-inputs
          class="margin"
          @save="saveEmprestimo" />
      </div>
    </template>
  </biblioteca-single-content-layout>
</template>

<script>
import { toastError } from '@/services/toastService';
import { EMPRESTIMO_ERRORS } from '@/modules/sala/sala.constants';
// eslint-disable-next-line import/no-cycle
import { goToOpenEmprestimo, goToEmprestimoNotFound } from '@/modules/sala/sala.routes';
import { saveEmprestimo, getEmprestimo } from '@/modules/sala/sala.service';

import BibliotecaEmprestimoEditInputs from '@/modules/sala/components/SalaEditInputs.vue';
import BibliotecaSingleContentLayout from '@/layouts/SingleContentLayout.vue';

export default {
  name: 'BibliotecaEmprestimoEditPage',
  components: {
    BibliotecaEmprestimoEditInputs,
    BibliotecaSingleContentLayout,
  },
  provide() {
    const emprestimoEditVm = {};
    Object.defineProperty(emprestimoEditVm, 'emprestimo', {
      get: () => this.emprestimo,
    });
    return { emprestimoEditVm };
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
    isEditing() {
      return !!this.emprestimo?.id;
    },
  },
  mounted() {
    if (this.id) {
      this.fetchEmprestimo();
    } else {
      this.emprestimo = {
        id_usuario: null,
        id_jogo: null,
        nome: null,
        descricao: null,
        hora: null,
        usuario_ids: [],
      };
    }
  },
  methods: {
    fetchEmprestimo() {
      getEmprestimo(this.id)
        .then(data => {
          this.emprestimo = data.data;
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
    saveEmprestimo() {
      console.log(this.emprestimo);
      saveEmprestimo(this.emprestimo)
        .then(data => {
          goToOpenEmprestimo(this.$router, data || this.emprestimo);
        })
        .catch(() => toastError('Erro ao salvar a sala'));
    },
  },
};
</script>
<style>
.titulo{
  text-align: center;
  font-family: 'sigmar';
  font-weight: 200;
}
.container{
  box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25) !important;
 border-radius: 20px !important;
}
.margin{
  margin: 0 4% 0 4%;
}
</style>
