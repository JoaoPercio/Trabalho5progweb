<template>
  <biblioteca-row class="usuario">
    <biblioteca-col
      :sm="1"
      :md="1">
    </biblioteca-col>
    <biblioteca-col
      :sm="10"
      :md="10">
      <biblioteca-header v-truncate size="sm" class="usuario2">
        <biblioteca-livro-link :id="livro.id">{{ livro.nome }}</biblioteca-livro-link>
      </biblioteca-header>
    </biblioteca-col>
  </biblioteca-row>
</template>

<script>
import BibliotecaLivroLink from '@/modules/jogo/components/JogoLink.vue';

export default {
  name: 'LivroListItem',
  components: {
    BibliotecaLivroLink,
  },
  props: {
    livro: {
      type: Object,
      required: true,
    },
  },
};
</script>
<style>
.usuario{
  background-color: #5E0CE3 !important;
  border: 1px solid black;
  color: black;
  padding: 5px;
}
.usuario2{
  margin-left: 2% !important;
  font-family: 'Sigmar';
  font-weight: 200 !important;
}
</style>
