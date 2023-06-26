<template>
  <div>
    <biblioteca-form v-if="emprestimoEditVm.emprestimo" :submit="save">
      <div class="form-field mt-4">
        <biblioteca-usuario-select
          ref="usuarioSelect"
          @on-change="onUsuarioChange" />
      </div>
      <div class="form-field mt-4">
        <biblioteca-livro-select
          ref="livroSelect"
          @on-change="onLivroChange" />
      </div>
      <div class="form-field mt-4">
        <label class="label-strong">Nome da sala</label>
        <biblioteca-input
          v-model="emprestimoEditVm.emprestimo.nome"
          label="Nome da sala"
          type="text"
          rules="required|min:2"
          placeholder="Nome" />
      </div>
      <div class="form-field mt-4">
        <label class="label-strong">Descrição</label>
        <biblioteca-textarea
          v-model="emprestimoEditVm.emprestimo.descricao"
          name="descricao"
          type="text"
          rules="required|min:2"
          placeholder="Descrição" />
      </div>
      <div class="form-field mt-4">
        <label class="label-strong">Data e Hora</label>
        <biblioteca-input
          v-model="emprestimoEditVm.emprestimo.hora"
          name="data hora"
          type="datetime-local"
          rules="required|min:2"
          placeholder="Descrição" />
      </div>

      <div class="mt-4 mb-3 d--flex justify-content-end">
        <biblioteca-button
          class="btn btn-secondary"
          width="110"
          size="sm"
          @click="goHistoryBack()">
          Cancelar
        </biblioteca-button>
        <biblioteca-button
          native-type="submit"
          class="btn btn-success ms-2"
          width="110"
          size="sm">
          <a v-if="emprestimoEditVm.emprestimo.id">Editar</a>
          <a v-else>Adicionar</a>
        </biblioteca-button>
      </div>
    </biblioteca-form>
  </div>
</template>

<script>
import { goHistoryBack } from '@/router/route.service';

import BibliotecaLivroSelect from '@/modules/jogo/components/JogoSelect.vue';
import BibliotecaUsuarioSelect from '@/modules/usuario/components/UsuarioSelect.vue';

export default {
  name: 'BibliotecaEmprestimoEdit',
  components: {
    BibliotecaLivroSelect,
    BibliotecaUsuarioSelect,
  },
  inject: ['emprestimoEditVm'],
  data() {
    return {
    };
  },
  methods: {
    goHistoryBack,
    save() {
      this.$emit('save');
    },
    onLivroChange(jogo) {
      this.emprestimoEditVm.emprestimo.id_jogo = jogo.id;
    },
    onUsuarioChange(usuario) {
      this.emprestimoEditVm.emprestimo.id_usuario = usuario.id;
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
