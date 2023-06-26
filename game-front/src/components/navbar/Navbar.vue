<template>
  <nav class="navbar">
    <slot name="brand">
      <a class="navbar-brand" href="/">
        <img alt="GamerFriends" height="56" src="@/assets/images/logo.png">
      </a>
    </slot>
    <div class="navbar-nav ms-auto">
      <ul v-if="$slots.right" class="navbar-nav ms-auto">
        <slot name="right" />
      </ul>
    </div>
  </nav>
</template>

<script>

export default {
  name: 'BibliotecaNavbar',
  props: {
    showBrand: {
      type: Boolean,
      default: true,
    },
  },
};
</script>
<style>
.navbar {
  background-color: #6404FF !important;
}

.biblioteca-container {
  margin-left: 10px;
}
</style>
