<template>
  <div>
    <div v-if="usuarios.length > 0">
      <div v-if="showLabel" class="label-strong">
        Usuário
      </div>
      <biblioteca-select
        v-bind="$attrs"
        name="usuário"
        rules="required"
        :class="showLabel ? 'mt--md' : ''"
        @on-change="onChange">
        <option :value="null" disabled>Selecione um usuário...</option>
        <option
          v-for="usuario in usuarios"
          :key="usuario.id"
          :value="usuario.id">
          {{ usuario.nome }}
        </option>
      </biblioteca-select>
    </div>
    <div v-else class="mb-3 mt-4">
      <biblioteca-p color="danger">
        *Você não possui usuários cadastrados
        <biblioteca-button @click="onCreate">
          Criar Usuário
        </biblioteca-button>
      </biblioteca-p>
    </div>
  </div>
</template>

<script>
import { fetchUsuarios } from '@/modules/usuario/usuario.service';
import { goToCreateUsuario } from '@/modules/usuario/usuario.routes';

export default {
  name: 'BibliotecaUsuarioSelect',
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
      usuarios: [],
    };
  },
  created() {
    this.onfetch();
  },
  methods: {
    onfetch() {
      fetchUsuarios()
        .then(({ data }) => {
          this.usuarios = data.data;
        })
        .catch(() => {
          this.usuarios = null;
        });
    },
    onChange(id) {
      this.$emit('on-change', { id });
    },
    onCreate() {
      goToCreateUsuario(this.$router);
    },
  },
};
</script>
<style>
.aa{
  border: 2px solid #6404FF !important;
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25)) !important;
}
.label-strong {
  font-weight: bold;
  font-size: 16px;
}
</style>
