<template>
  <biblioteca-row class="usuario">
    <biblioteca-col
      :sm="4"
      :md="2">
    </biblioteca-col>
    <biblioteca-col
      :sm="20"
      :md="22">
      <biblioteca-header v-truncate size="sm" class="usuario2">
        <biblioteca-emprestimo-link :id="emprestimo.id">{{ emprestimo.nome }}</biblioteca-emprestimo-link>
      </biblioteca-header>
      <div v-if="showDetails">
        <biblioteca-p color="black">
          <Strong>Dono: </Strong>{{ emprestimo.usuario.nome }}
        </biblioteca-p>
        <biblioteca-p color="black">
          <Strong>Jogo: </Strong>{{ emprestimo.jogo.nome }}
        </biblioteca-p>
        <biblioteca-p color="black">
          <Strong>Descriçao: </Strong>{{ emprestimo.descricao }}
        </biblioteca-p>
        <biblioteca-p color="black">
          <Strong>Data e hora: </Strong>{{ formatarData(emprestimo.hora) }}
        </biblioteca-p>
      </div>
    </biblioteca-col>
    <i class="bi bi-chevron-down bi-200x custom-dropdown-icon" @click="toggleDetails"></i>
  </biblioteca-row>
</template>

<script>
import moment from 'moment';

import BibliotecaEmprestimoLink from '@/modules/sala/components/SalaLink.vue';

export default {
  name: 'EmprestimoListItem',
  components: {
    BibliotecaEmprestimoLink,
  },
  props: {
    emprestimo: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      showDetails: false,
    };
  },
  methods: {
    toggleDetails() {
      this.showDetails = !this.showDetails;
    },
    formatarData(data) {
      return moment(data).format('DD/MM/YYYY HH:mm');
    },
  },
};
</script>
<style>
.usuario{
  background-color: #5E0CE3 !important;
  border: 1px solid black;
  color: black;
}
strong{
  margin-left: 2% !important;
}
.custom-dropdown-icon {
  font-size: 1.6rem; /* Tamanho personalizado do ícone de dropdown */
}
</style>
