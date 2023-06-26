export const LIVROS_URL = Object.freeze({
  path: '/jogos',
  view: {
    name: 'jogo.view',
    path: '/jogos/ver/:id',
  },
  edit: {
    name: 'jogo.edit',
    path: '/jogos/editar/:id',
  },
  create: {
    name: 'jogo.create',
    path: '/jogos/criar',
  },
  notfound: {
    name: 'jogo.notfound',
    path: '/jogos/nao-encontrado',
  },
});

export const LIVRO_ERRORS = {
  404: 'LIVRO_NOT_FOUND',
  401: 'PERMISSION_DENIED',
};
