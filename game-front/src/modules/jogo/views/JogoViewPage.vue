<template>
  <biblioteca-single-content-layout container-size="lg">
    <template v-if="livro" #content>
      <biblioteca-row class="d-flex align-items-center">
        <biblioteca-col>
          <biblioteca-header>
            {{ livro.nome }}
          </biblioteca-header>
        </biblioteca-col>
      </biblioteca-row>
      <biblioteca-row class="mt-1">
        <biblioteca-col>
          <biblioteca-p class="biblioteca-u-text--medium">
            {{ livro.resumo }}
          </biblioteca-p>
        </biblioteca-col>
      </biblioteca-row>
    </template>
  </biblioteca-single-content-layout>
</template>

<script>
import { LIVRO_ERRORS } from '@/modules/jogo/jogo.constants';
import { getLivro } from '@/modules/jogo/jogo.service';
import { toastError } from '@/services/toastService';
// eslint-disable-next-line import/no-cycle
import { goToLivroNotFound } from '@/modules/jogo/jogo.routes';
import BibliotecaSingleContentLayout from '@/layouts/SingleContentLayout.vue';

export default {
  name: 'LivroViewPage',
  components: {
    BibliotecaSingleContentLayout,
  },
  data() {
    return {
      livro: null,
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
      getLivro(this.id)
        .then(({ data }) => {
          this.livro = data;
        })
        .catch(err => {
          this.livro = null;
          if (err) {
            goToLivroNotFound(this.$router);
          } else if ((err.response.data.errors === LIVRO_ERRORS[err.response.status] && err.response.status === 404)) {
            goToLivroNotFound(this.$router);
          } else {
            toastError('Erro ao buscar o jogo');
          }
        });
    },
  },
};
</script>
