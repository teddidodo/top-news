const routes = [
  {
    path: '/',
    component: () => import('@/layouts/AccountLayout.vue'),
    children: [
      {
        path: '',
        component: () => import('@/views/Home.vue'),
      },
      // {
      //   path: 'profile/:username',
      //   name: 'profile',
      //   component: () => import('../views/Profile.vue')
      // },
      {
        path: 'login',
        name: 'login',
        component: () => import('../views/Login.vue')
      },
      {
        path: 'register',
        name: 'register',
        component: () => import('../views/Register.vue')
      }
    ]
  },
  {
    path: '/news',
    component: () => import('@/layouts/Layout.vue'),
    children: [
      {
        path: '',
        name: 'news',
        component: () => import('../views/Search.vue')

      },
    ]
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not_found',
    component: () => import('@/views/NotFound.vue'),
  }

];

export default routes;
