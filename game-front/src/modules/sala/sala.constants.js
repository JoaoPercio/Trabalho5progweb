export const EMPRESTIMOS_URL = Object.freeze({
  path: '/salas',
  view: {
    name: 'sala.view',
    path: '/salas/ver/:id',
  },
  edit: {
    name: 'sala.edit',
    path: '/salas/editar/:id',
  },
  create: {
    name: 'sala.create',
    path: '/salas/criar',
  },
  notfound: {
    name: 'sala.notfound',
    path: '/salas/nao-encontrado',
  },
});

export const EMPRESTIMO_ERRORS = {
  404: 'EMPRESTIMO_NOT_FOUND',
  401: 'PERMISSION_DENIED',
};
