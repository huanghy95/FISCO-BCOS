<template>
  <CToaster placement="top-end">
    <CToast v-for="(toast, index) in toasts">
      <CToastHeader closeButton>
        <span class="me-auto fw-bold">{{ toast.title }}</span>
      </CToastHeader>
      <CToastBody>
        {{ toast.content }}
      </CToastBody>
    </CToast>
  </CToaster>
  <CRow>
    <CCol :xs="12">
      <CCallout color="dark">
        <font size="6"><strong>账户查询</strong></font>
      </CCallout>
    </CCol>

    <CCol :xs="12">
      <CContainer>
        <p class="text-medium-emphasis medium">
          说明: 在当前页面，可以通过输入给定账户的地址，查询该账户的相关信息
        </p>
      </CContainer>

      <CCard class="mb-4">
        <CCardHeader>
          <font size="5"><strong>信用值查询</strong></font>
        </CCardHeader>
        <CCardBody>
          <p>
            <font size="4" color="#3399ff"><strong>数据输入</strong></font>
            <br />
          </p>
          <CTable>
            <CTableHead color="secondary">
              <CTableRow>
                <CTableHeaderCell scope="col" style="width: 200px"
                  >属性</CTableHeaderCell
                >
                <CTableHeaderCell scope="col">输出</CTableHeaderCell>
                <CTableHeaderCell scope="col" class="right" style="width: 400px"
                  >说明</CTableHeaderCell
                >
              </CTableRow>
            </CTableHead>
            <CTableBody>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">地址</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="address"
                    v-model="getAccountValueAddress"
                /></CTableDataCell>
                <CTableDataCell>当前账户的信用值</CTableDataCell>
              </CTableRow>
            </CTableBody>
          </CTable>
          <CContainer>
            <CRow>
              <CCol class="align-self-start"></CCol>
              <CCol class="align-self-center">
                <div class="d-grid">
                  <CButton
                    color="info"
                    class="align-self-center"
                    v-on:click="getAccountValue"
                    >查询</CButton
                  >
                </div></CCol
              >
              <CCol class="align-self-end"></CCol>
            </CRow>
          </CContainer>
          <br />
          <p>
            <font size="4" color="#3399ff"><strong>查询结果</strong></font>
            <br />
          </p>
          <CTable style="padding-top: 10px">
            <CTableHead color="secondary">
              <CTableRow>
                <CTableHeaderCell scope="col" style="width: 200px"
                  >属性</CTableHeaderCell
                >
                <CTableHeaderCell scope="col">输出</CTableHeaderCell>
                <CTableHeaderCell scope="col" class="right" style="width: 400px"
                  >说明</CTableHeaderCell
                >
              </CTableRow>
            </CTableHead>
            <CTableBody>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">信用值</CTableHeaderCell>
                <CTableDataCell>{{ accountValue }}</CTableDataCell>
                <CTableDataCell>当前账户的信用值</CTableDataCell>
              </CTableRow>
            </CTableBody>
          </CTable>
        </CCardBody>
      </CCard>

      <CCard class="mb-4">
        <CCardHeader>
          <font size="5"><strong>账户类型查询</strong></font>
        </CCardHeader>
        <CCardBody>
          <p>
            <font size="4" color="#3399ff"><strong>数据输入</strong></font>
            <br />
          </p>
          <CTable>
            <CTableHead color="secondary">
              <CTableRow>
                <CTableHeaderCell scope="col" style="width: 200px"
                  >属性</CTableHeaderCell
                >
                <CTableHeaderCell scope="col">输出</CTableHeaderCell>
                <CTableHeaderCell scope="col" class="right" style="width: 400px"
                  >说明</CTableHeaderCell
                >
              </CTableRow>
            </CTableHead>
            <CTableBody>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">地址</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="address"
                    v-model="getAccountTypeAddress"
                /></CTableDataCell>
                <CTableDataCell>当前账户的类型</CTableDataCell>
              </CTableRow>
            </CTableBody>
          </CTable>
          <CContainer>
            <CRow>
              <CCol class="align-self-start"></CCol>
              <CCol class="align-self-center">
                <div class="d-grid">
                  <CButton
                    color="info"
                    class="align-self-center"
                    v-on:click="getAccountType"
                    >查询</CButton
                  >
                </div></CCol
              >
              <CCol class="align-self-end"></CCol>
            </CRow>
          </CContainer>
          <br />
          <p>
            <font size="4" color="#3399ff"><strong>查询结果</strong></font>
            <br />
          </p>
          <CTable style="padding-top: 10px">
            <CTableHead color="secondary">
              <CTableRow>
                <CTableHeaderCell scope="col" style="width: 200px"
                  >属性</CTableHeaderCell
                >
                <CTableHeaderCell scope="col">输出</CTableHeaderCell>
                <CTableHeaderCell scope="col" class="right" style="width: 400px"
                  >说明</CTableHeaderCell
                >
              </CTableRow>
            </CTableHead>
            <CTableBody>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">账户类型</CTableHeaderCell>
                <CTableDataCell>{{ accountType }}</CTableDataCell>
                <CTableDataCell>当前账户的账户类型</CTableDataCell>
              </CTableRow>
            </CTableBody>
          </CTable>
        </CCardBody>
      </CCard>
    </CCol>
  </CRow>
</template>

<script>
export default {
  name: 'Account',
  data() {
    return { accountValue: 0, toasts: [], accountType: '' }
  },
  methods: {
    success() {
      this.toasts.push({
        title: '查询成功',
        content: '查询结果已写入表格',
      })
    },
    fail() {
      this.toasts.push({
        title: '查询出错',
        content: '请输出正确的数据',
      })
    },
    getAccountValue: function () {
      var that = this
      this.$http({
        method: 'post',
        url: 'api/account/accountValue',
        data: { address: this.getAccountValueAddress },
      })
        .then((res) => {
          this.accountValue = res['data']['accountValue']
          that.success()
        })
        .catch(function (error) {
          that.fail()
        })
    },
    getAccountType: function () {
      var that = this
      console.log(this.getAccountTypeAddress)
      this.$http({
        method: 'post',
        url: 'api/account/accountType',
        data: { address: this.getAccountTypeAddress },
      })
        .then((res) => {
          this.accountType = res['data']['accountType']
          that.success()
        })
        .catch(function (error) {
          that.fail()
        })
    },
  },
}
</script>
