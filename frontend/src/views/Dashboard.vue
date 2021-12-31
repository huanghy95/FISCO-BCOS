<template>
  <div>
    <CRow>
      <CCol :md="12">
        <CCardBody class="text-center">
          <div>
            <h2>欢迎来到基于区块链的供应链金融平台!</h2>
          </div>
        </CCardBody>
      </CCol>
    </CRow>
    <CRow>
      <CCol :xs="4">
        <CWidgetStatsC
          class="mb-3"
          value="Account"
          inverse
          color="info"
          title="账户查询"
        >
          <template #icon><CIcon icon="cil-people" height="36" /></template>
        </CWidgetStatsC>
        <CLink
          class="font-weight-bold font-xs text-medium-emphasis"
          href="#/account"
          rel="noopener norefferer"
          target="_blank"
        >
          进入账户查询界面
          <CIcon icon="cil-arrow-right" class="ms-auto" width="16" />
        </CLink>
      </CCol>

      <CCol :xs="4">
        <CWidgetStatsC
          class="mb-3"
          value="Bill-Query"
          inverse
          color="info"
          title="交易查询"
        >
          <template #icon><CIcon icon="cil-money" height="36" /></template>
        </CWidgetStatsC>
        <CLink
          class="font-weight-bold font-xs text-medium-emphasis"
          href="#/bill/query"
          rel="noopener norefferer"
          target="_blank"
        >
          进入交易查询界面
          <CIcon icon="cil-arrow-right" class="ms-auto" width="16" />
        </CLink>
      </CCol>
      <CCol :xs="4">
        <CWidgetStatsC
          class="mb-3"
          value="Bill-Transaction"
          inverse
          color="info"
          title="发起交易"
        >
          <template #icon><CIcon icon="cil-money" height="36" /></template>
        </CWidgetStatsC>
        <CLink
          class="font-weight-bold font-xs text-medium-emphasis"
          href="#/bill/transaction"
          rel="noopener norefferer"
          target="_blank"
        >
          进入发起交易界面
          <CIcon icon="cil-arrow-right" class="ms-auto" width="16" />
        </CLink>
      </CCol>
    </CRow>
  </div>
</template>

<script>
import avatar1 from '@/assets/images/avatars/1.jpg'
import avatar2 from '@/assets/images/avatars/2.jpg'
import avatar3 from '@/assets/images/avatars/3.jpg'
import avatar4 from '@/assets/images/avatars/4.jpg'
import avatar5 from '@/assets/images/avatars/5.jpg'
import avatar6 from '@/assets/images/avatars/6.jpg'
import MainChartExample from './charts/MainChartExample'
import WidgetsStatsA from './widgets/WidgetsStatsTypeA.vue'
import WidgetsStatsD from './widgets/WidgetsStatsTypeD.vue'

export default {
  name: 'Dashboard',
  components: {
    MainChartExample,
    WidgetsStatsA,
    WidgetsStatsD,
  },
  method: {
    account: function () {
      this.$router.push({
        path: '/account',
      })
    },
  },
}
</script>
