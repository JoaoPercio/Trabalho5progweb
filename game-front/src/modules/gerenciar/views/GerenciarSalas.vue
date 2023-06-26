<template>
  <biblioteca-single-content-layout container-size="lg">
    <template #content>
      <div class="d--flex justify-content--space-between align-items--center">
        <biblioteca-header class="titulo">Salas</biblioteca-header>
        <biblioteca-button @click="onCreateEmprestimo">
          Criar sala
        </biblioteca-button>
      </div>
      <table v-if="emprestimoList && emprestimoList.length > 0" class="table">
        <tbody>
          <tr v-for="emprestimo in emprestimoList" :key="emprestimo.id">
            <td class="py-3 px-2">
              <biblioteca-header size="sm" class="d-flex align-item--center">
                <biblioteca-emprestimo-link :id="emprestimo.id">
                  {{ emprestimo.nome }}
                </biblioteca-emprestimo-link>
              </biblioteca-header>
              <biblioteca-p color="regular">
                Dono: {{ emprestimo.usuario.nome }}
              </biblioteca-p>
              <biblioteca-p color="regular">
                Jogo: {{ emprestimo.jogo.nome }}
              </biblioteca-p>
              <biblioteca-p color="regular">
                Descricao: {{ emprestimo.descricao }}
              </biblioteca-p>
              <biblioteca-p color="regular">
                Data: {{ formatarData(emprestimo.hora) }}
              </biblioteca-p>
            </td>
            <td class="align-middle text-end">
              <el-dropdown
                trigger="click">
                <biblioteca-icon
                  icon="three-dots-vertical"
                  class="cursor--pointer mx--md" />
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item>
                    <biblioteca-emprestimo-link :id="emprestimo.id" action="edit">
                      <biblioteca-icon size="sm" icon="pencil" />
                      Editar
                    </biblioteca-emprestimo-link>
                  </el-dropdown-item>
                  <el-dropdown-item>
                    <a @click="setDeleteUsuario(emprestimo)">
                      <biblioteca-icon size="sm" icon="trash" />
                      Excluir
                    </a>
                  </el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
              <biblioteca-modal-delete
                v-if="showModal(emprestimo)"
                content="Você realmente deseja excluir a sala?"
                @close="setDeleteUsuario(null)"
                @confirm="onDeleteUsuario(emprestimo)">
              </biblioteca-modal-delete>
            </td>
          </tr>
        </tbody>
      </table>
      <biblioteca-p v-else class="opacity--50 my--lg">( Sem salas )</biblioteca-p>
    </template>
  </biblioteca-single-content-layout>
</template>

<script>
import moment from 'moment';

import { toastError } from '@/services/toastService';
import { fetchEmprestimos, removeEmprestimo } from '@/modules/sala/sala.service';
import { goToCreateEmprestimo } from '@/modules/sala/sala.routes';

import BibliotecaEmprestimoLink from '@/modules/sala/components/SalaLink.vue';
import BibliotecaSingleContentLayout from '@/layouts/SingleContentLayout.vue';

export default {
  name: 'BibliotecaGerenciarEmprestimos',
  components: {
    BibliotecaEmprestimoLink,
    BibliotecaSingleContentLayout,
  },
  data() {
    return {
      emprestimoList: [],
      emprestimoDelete: null,
    };
  },
  mounted() {
    this.fetch();
  },
  methods: {
    fetch() {
      this.emprestimoList = [];
      fetchEmprestimos()
        .then(({ data }) => {
          this.emprestimoList = data.data;
        })
        .catch(() => {
          this.emprestimoList = [];
        });
    },
    onCreateEmprestimo() {
      goToCreateEmprestimo(this.$router);
    },
    setDeleteUsuario(emprestimo) {
      this.emprestimoDelete = emprestimo;
    },
    showModal(emprestimo) {
      return this.emprestimoDelete && this.emprestimoDelete.id === emprestimo.id;
    },
    onDeleteUsuario(emprestimo) {
      removeEmprestimo(emprestimo)
        .then(() => {
          this.$router.go(0);
        })
        .catch(() => toastError('Não foi possível excluir a sala'));
    },
    formatarData(data) {
      return moment(data).format('DD/MM/YYYY');
    },
  },
};
</script>
<style>
button{
  background-color: #5E0CE3 !important;
  color: white !important;
}
.titulo{
  color:#5E0CE3;
}
</style>
