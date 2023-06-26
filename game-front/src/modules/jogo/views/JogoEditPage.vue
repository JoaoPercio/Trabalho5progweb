<template>
  <biblioteca-single-content-layout container-size="lg">
    <template #content>
      <biblioteca-header v-if="isEditing">
        Editar Jogo
      </biblioteca-header>
      <biblioteca-header v-else>
        Criar Jogo
      </biblioteca-header>
      <biblioteca-livro-edit-inputs @save="saveLivro" />
    </template>
  </biblioteca-single-content-layout>
</template>

<script>
import { toastError } from '@/services/toastService';
import { LIVRO_ERRORS } from '@/modules/jogo/jogo.constants';
// eslint-disable-next-line import/no-cycle
import { goToOpenLivro, goToLivroNotFound } from '@/modules/jogo/jogo.routes';
import { saveLivro, getLivro } from '@/modules/jogo/jogo.service';

import BibliotecaLivroEditInputs from '@/modules/jogo/components/JogoEditInputs.vue';
import BibliotecaSingleContentLayout from '@/layouts/SingleContentLayout.vue';

export default {
  name: 'BibliotecaLivroEditPage',
  components: {
    BibliotecaLivroEditInputs,
    BibliotecaSingleContentLayout,
  },
  provide() {
    const livroEditVm = {};
    Object.defineProperty(livroEditVm, 'livro', {
      get: () => this.livro,
    });
    return { livroEditVm };
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
    isEditing() {
      return !!this.livro?.id;
    },
  },
  mounted() {
    if (this.id) {
      this.fetchLivro();
    } else {
      this.livro = {};
    }
  },
  methods: {
    fetchLivro() {
      getLivro(this.id)
        .then(data => {
          this.livro = data.data;
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
    saveLivro() {
      saveLivro(this.livro)
        .then(data => {
          goToOpenLivro(this.$router, data || this.livro);
        })
        .catch(() => toastError('Erro ao salvar o jogo'));
    },
  },
};
</script>
