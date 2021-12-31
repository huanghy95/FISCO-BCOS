export default [
  {
    component: 'CNavItem',
    name: 'Dashboard',
    to: '/dashboard',
    icon: 'cil-speedometer',
  },
  {
    component: 'CNavItem',
    name: 'Account',
    to: '/account',
    icon: 'cilUser',
  },
  {
    component: 'CNavItem',
    name: 'Bill',
    to: '/bill',
    icon: 'cilMoney',
    items: [
      {
        component: 'CNavItem',
        name: 'Query',
        to: '/bill/query',
      },
      {
        component: 'CNavItem',
        name: 'Transaction',
        to: '/bill/transaction',
      },
    ],
  },

  // {
  //   component: 'CNavItem',
  //   name: 'Download CoreUI',
  //   href: 'http://coreui.io/vue/',
  //   icon: { name: 'cil-cloud-download', class: 'text-white' },
  //   _class: 'bg-success text-white',
  //   target: '_blank'
  // },
  // {
  //   component: 'CNavItem',
  //   name: 'Try CoreUI PRO',
  //   href: 'http://coreui.io/pro/vue/',
  //   icon: { name: 'cil-layers', class: 'text-white' },
  //   _class: 'bg-danger text-white',
  //   target: '_blank'
  // }
]
