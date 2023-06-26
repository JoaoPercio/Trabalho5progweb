<template>
  <div>
    <div v-if="livros.length > 0">
      <div v-if="showLabel" class="label-strong">
        Jogo
      </div>
      <biblioteca-select
        v-bind="$attrs"
        name="jogo"
        rules="required"
        :class="showLabel ? 'mt--md' : ''"
        @on-change="onChange">
        <option :value="null" disabled>Selecione um jogo...</option>
        <option
          v-for="livro in livros"
          :key="livro.id"
          :value="livro.id">
          {{ livro.nome }}
        </option>
      </biblioteca-select>
    </div>
    <div v-else class="mb-3 mt-4">
      <biblioteca-p color="danger">
        *Não existem jogos cadastrados
        <biblioteca-button @click="onCreate">
          Criar Jogo
        </biblioteca-button>
      </biblioteca-p>
    </div>
  </div>
</template>

<script>
import { fetchLivros } from '@/modules/jogo/jogo.service';
import { goToCreateLivro } from '@/modules/jogo/jogo.routes';

export default {
  name: 'BibliotecaLivroSelect',
  props: {
    showLabel: {
      type: Boolean,
      default: true,
    },
    isFilter: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      livros: [],
    };
  },
  created() {
    this.onfetch();
  },
  methods: {
    onfetch() {
      fetchLivros()
        .then(({ data }) => {
          this.livros = data.data;
        })
        .catch(() => {
          this.livros = null;
        });
    },
    onChange(id) {
      this.$emit('on-change', { id });
    },
    onCreate() {
      goToCreateLivro(this.$router);
    },
  },
};
</script>
<style>
.label-strong {
  font-weight: bold;
  font-size: 16px;
}
</style>
