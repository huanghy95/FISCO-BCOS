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
        <font size="6"><strong>交易查询</strong></font>
      </CCallout>
    </CCol>

    <CCol :xs="12">
      <CContainer>
        <p class="text-medium-emphasis medium">
          说明: 在当前页面，可以查询债务的相关信息
        </p>
      </CContainer>

      <CCard class="mb-4">
        <CCardHeader>
          <font size="5"><strong>债务人查询</strong></font>
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
                <CTableHeaderCell scope="row">账单编号</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput placeholder="bill ID" v-model="getBillDebtorID"
                /></CTableDataCell>
                <CTableDataCell>当前账单的债务人</CTableDataCell>
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
                    v-on:click="getBillDebtor"
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
                <CTableHeaderCell scope="row">地址</CTableHeaderCell>
                <CTableDataCell>{{ debtorAddress }}</CTableDataCell>
                <CTableDataCell>当前账单的债务人地址</CTableDataCell>
              </CTableRow>
            </CTableBody>
          </CTable>
        </CCardBody>
      </CCard>

      <CCard class="mb-4">
        <CCardHeader>
          <font size="5"><strong>债权人查询</strong></font>
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
                <CTableHeaderCell scope="row">账单编号</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="bill ID"
                    v-model="getBillCreditorID"
                /></CTableDataCell>
                <CTableDataCell>当前账单的债权人</CTableDataCell>
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
                    v-on:click="getBillCreditor"
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
                <CTableHeaderCell scope="row">地址</CTableHeaderCell>
                <CTableDataCell>{{ creditorAddress }}</CTableDataCell>
                <CTableDataCell>当前账单的债权人地址</CTableDataCell>
              </CTableRow>
            </CTableBody>
          </CTable>
        </CCardBody>
      </CCard>

      <CCard class="mb-4">
        <CCardHeader>
          <font size="5"><strong>账单额度查询</strong></font>
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
                <CTableHeaderCell scope="row">账单编号</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput placeholder="bill ID" v-model="getBillValueID"
                /></CTableDataCell>
                <CTableDataCell>当前账单的编号</CTableDataCell>
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
                    v-on:click="getBillValue"
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
                <CTableHeaderCell scope="row">账单额度</CTableHeaderCell>
                <CTableDataCell>{{ billValue }}</CTableDataCell>
                <CTableDataCell>当前账单的账单额度</CTableDataCell>
              </CTableRow>
            </CTableBody>
          </CTable>
        </CCardBody>
      </CCard>

      <CCard class="mb-4">
        <CCardHeader>
          <font size="5"><strong>账单状态查询</strong></font>
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
                <CTableHeaderCell scope="row">账单编号</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput placeholder="bill ID" v-model="getBillStatusID"
                /></CTableDataCell>
                <CTableDataCell>当前账单的编号</CTableDataCell>
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
                    v-on:click="getBillStatus"
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
                <CTableHeaderCell scope="row">账单状态</CTableHeaderCell>
                <CTableDataCell>{{ billStatus }}</CTableDataCell>
                <CTableDataCell>当前账单的账单状态</CTableDataCell>
              </CTableRow>
            </CTableBody>
          </CTable>
        </CCardBody>
      </CCard>

      <CCard class="mb-4">
        <CCardHeader>
          <font size="5"><strong>债务人所有账单查询</strong></font>
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
                    v-model="queryBillDebtorAddress"
                /></CTableDataCell>
                <CTableDataCell>给定债务人的地址</CTableDataCell>
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
                    v-on:click="queryBillDebtor"
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
                <CTableHeaderCell scope="row">所有账单编号</CTableHeaderCell>
                <CTableDataCell>{{ debtorBillIDs }}</CTableDataCell>
                <CTableDataCell>给定债务人的所有账单编号</CTableDataCell>
              </CTableRow>
            </CTableBody>
          </CTable>
        </CCardBody>
      </CCard>

      <CCard class="mb-4">
        <CCardHeader>
          <font size="5"><strong>债权人所有账单查询</strong></font>
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
                    v-model="queryBillCreditorAddress"
                /></CTableDataCell>
                <CTableDataCell>给定债务人的地址</CTableDataCell>
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
                    v-on:click="queryBillCreditor"
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
                <CTableHeaderCell scope="row">所有账单编号</CTableHeaderCell>
                <CTableDataCell>{{ creditorBillIDs }}</CTableDataCell>
                <CTableDataCell>给定债权人的所有账单编号</CTableDataCell>
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
    return {
      debtorAddress: '',
      toasts: [],
      creditorAddress: '',
      billValue: '',
      billStatus: '',
      queryBillDebtorAddress: '',
      billIDs: '',
    }
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
    getBillDebtor: function () {
      var that = this
      this.$http({
        method: 'post',
        url: 'api/bill/billDebtor',
        data: { id: this.getBillDebtorID },
      })
        .then((res) => {
          this.debtorAddress = res['data']['debtor address']
          that.success()
        })
        .catch(function (error) {
          that.fail()
        })
    },
    getBillCreditor: function () {
      var that = this
      this.$http({
        method: 'post',
        url: 'api/bill/billCreditor',
        data: { id: this.getBillCreditorID },
      })
        .then((res) => {
          this.creditorAddress = res['data']['creditor address']
          that.success()
        })
        .catch(function (error) {
          that.fail()
        })
    },
    getBillValue: function () {
      var that = this
      this.$http({
        method: 'post',
        url: 'api/bill/billValue',
        data: { id: this.getBillValueID },
      })
        .then((res) => {
          this.billValue = res['data']['bill value']
          that.success()
        })
        .catch(function (error) {
          that.fail()
        })
    },
    getBillStatus: function () {
      var that = this
      this.$http({
        method: 'post',
        url: 'api/bill/billStatus',
        data: { id: this.getBillStatusID },
      })
        .then((res) => {
          this.billStatus = res['data']['bill status']
          that.success()
        })
        .catch(function (error) {
          that.fail()
        })
    },
    queryBillDebtor: function () {
      var that = this
      this.$http({
        method: 'post',
        url: 'api/bill/queryBillDebtor',
        data: { address: this.queryBillDebtorAddress },
      })
        .then((res) => {
          this.debtorBillIDs = res['data']['credited bill IDs']
          that.success()
        })
        .catch(function (error) {
          that.fail()
        })
    },
    queryBillCreditor: function () {
      var that = this
      this.$http({
        method: 'post',
        url: 'api/bill/queryBillCreditor',
        data: { address: this.queryBillCreditorAddress },
      })
        .then((res) => {
          this.creditorBillIDs = res['data']['credited bill IDs']
          that.success()
        })
        .catch(function (error) {
          that.fail()
        })
    },
  },
}
</script>
