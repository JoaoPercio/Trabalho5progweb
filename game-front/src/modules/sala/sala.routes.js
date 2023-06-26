import { EMPRESTIMOS_URL } from '@/modules/sala/sala.constants';
import { createEmptyComponent } from '@/router/route.service';

export default [
  {
    path: EMPRESTIMOS_URL.path,
    redirect: '/',
    component: { render: createEmptyComponent },
    children: [
      {
        ...EMPRESTIMOS_URL.view,
        component: () => import('@/modules/sala/views/SalaViewPage.vue'),
      },
      {
        ...EMPRESTIMOS_URL.edit,
        component: () => import('@/modules/sala/views/SalaEditPage.vue'),
      },
      {
        ...EMPRESTIMOS_URL.create,
        component: () => import('@/modules/sala/views/SalaEditPage.vue'),
      },
      {
        ...EMPRESTIMOS_URL.notfound,
        component: () => import('@/modules/sala/views/SalaNotFound.vue'),
      },
    ],
  },
];

export function goToEmprestimoNotFound($router) {
  $router.push({
    name: EMPRESTIMOS_URL.notfound.name,
  });
}

export function goToOpenEmprestimo($router, emprestimo) {
  $router.push({
    name: EMPRESTIMOS_URL.view.name,
    params: { id: emprestimo.id },
  });
}

export function goToCreateEmprestimo($router) {
  $router.push({
    name: EMPRESTIMOS_URL.create.name,
  });
}
