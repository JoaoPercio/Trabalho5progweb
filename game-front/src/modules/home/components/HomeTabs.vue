<template>
  <el-tabs v-model="tabActive" class="tab" @tab-click="fetch">
    <el-tab-pane label="Salas" name="salas" class="tab">
      <div v-if="emprestimoList.length">
        <div
          v-for="emprestimo in emprestimoList"
          :key="emprestimo.id"
          class="mb-3">
          <biblioteca-emprestimo-card :emprestimo="emprestimo" />
        </div>
      </div>
      <div v-else>
        <biblioteca-p class="opacity--50 my--md">( Sem salas )</biblioteca-p>
      </div>
    </el-tab-pane>
    <el-tab-pane label="Jogos" name="jogos" class="tab">
      <div v-if="livroList.length">
        <div
          v-for="livro in livroList"
          :key="livro.id"
          class="mb-3">
          <biblioteca-livro-card :livro="livro" />
        </div>
      </div>
      <div v-else>
        <biblioteca-p class="opacity--50 my--md">( Sem livros )</biblioteca-p>
      </div>
    </el-tab-pane>
    <el-tab-pane label="Usuários" name="usuarios" class="tab">
      <div v-if="usuarioList.length">
        <div
          v-for="usuario in usuarioList"
          :key="usuario.id"
          class="mb-3">
          <biblioteca-usuario-card :usuario="usuario" />
        </div>
      </div>
      <div v-else>
        <biblioteca-p class="opacity--50 my--md">( Sem usuários )</biblioteca-p>
      </div>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
import { fetchUsuarios } from '@/modules/usuario/usuario.service';
import { fetchLivros } from '@/modules/jogo/jogo.service';
import { fetchEmprestimos } from '@/modules/sala/sala.service';

import BibliotecaUsuarioCard from '@/modules/usuario/components/UsuarioCard.vue';
import BibliotecaLivroCard from '@/modules/jogo/components/JogoCard.vue';
import BibliotecaEmprestimoCard from '@/modules/sala/components/SalaCard.vue';

export default {
  name: 'BibliotecaHomeTabs',
  components: {
    BibliotecaUsuarioCard,
    BibliotecaLivroCard,
    BibliotecaEmprestimoCard,
  },
  data() {
    return {
      tabActive: 'salas',
      usuarioList: [],
      livroList: [],
      emprestimoList: [],
    };
  },
  mounted() {
    this.fetch();
  },
  methods: {
    fetch() {
      if (this.tabActive === 'salas') {
        this.fetchEmprestimos();
      } else if (this.tabActive === 'jogos') {
        this.fetchLivros();
      } else if (this.tabActive === 'usuarios') {
        this.fetchUsuarios();
      }
    },
    fetchLivros() {
      fetchLivros()
        .then(({ data }) => {
          this.livroList = data.data;
        })
        .catch(() => {
          this.livroList = [];
        });
    },
    fetchUsuarios() {
      fetchUsuarios()
        .then(({ data }) => {
          this.usuarioList = data.data;
        })
        .catch(() => {
          this.usuarioList = [];
        });
    },
    fetchEmprestimos() {
      fetchEmprestimos()
        .then(({ data }) => {
          this.emprestimoList = data.data;
        })
        .catch(() => {
          this.emprestimoList = [];
        });
    },
  },
};
</script>
<style>
</style>
