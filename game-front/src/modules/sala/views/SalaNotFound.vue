<template>
  <biblioteca-single-content-layout container-size="md">
    <template #content>
      <div class="d-flex align-items--center direction--column">
        <biblioteca-icon size="xxl" icon="question-octagon" />
        <biblioteca-header>Sala não encontrada</biblioteca-header>
        <biblioteca-p>
          Erro ao localizar a sala.
        </biblioteca-p>
        <br>
        <biblioteca-button theme="primary" @click="goToBasePage()">
          Retornar para Home
        </biblioteca-button>
      </div>
    </template>
  </biblioteca-single-content-layout>
</template>

<script>
import { goToBasePage } from '@/router/route.service';
import BibliotecaSingleContentLayout from '@/layouts/SingleContentLayout.vue';

export default {
  name: 'BibliotecaEmprestimoNotFoundPage',
  components: {
    BibliotecaSingleContentLayout,
  },
  methods: {
    goToBasePage,
  },
};
</script>
