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
        <biblioteca-usuario-link :id="usuario.id">{{ usuario.nome }}</biblioteca-usuario-link>
      </biblioteca-header>
    </biblioteca-col>
  </biblioteca-row>
</template>

<script>
import BibliotecaUsuarioLink from '@/modules/usuario/components/UsuarioLink.vue';

export default {
  name: 'UsuarioCard',
  components: {
    BibliotecaUsuarioLink,
  },
  props: {
    usuario: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
    };
  },
  computed: {
  },
};
</script>
<style>
.usuario{
  background-color: #5E0CE3 !important;
  border: 1px solid black;
  color: black;
  border-radius: 5px;
}
.usuario2{
  margin-left: 2% !important;
}
</style>
