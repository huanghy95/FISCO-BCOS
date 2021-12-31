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
        <font size="6"><strong>发起交易</strong></font>
      </CCallout>
    </CCol>

    <CCol :xs="12">
      <CContainer>
        <p class="text-medium-emphasis medium">
          说明: 在当前页面，可以发起融资交易
        </p>
      </CContainer>

      <CCard class="mb-4">
        <CCardHeader>
          <font size="5"><strong>添加账单</strong></font>
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
                <CTableHeaderCell scope="row">债务人地址</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="debtorAddress"
                    v-model="addBillAddress"
                /></CTableDataCell>
                <CTableDataCell>该账单的债务人地址</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">债务人私钥</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput placeholder="privkey" v-model="addBillPrivkey"
                /></CTableDataCell>
                <CTableDataCell>该账单的债务人私钥</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">债权人地址</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="creditorAddress"
                    v-model="addBillCreditor"
                /></CTableDataCell>
                <CTableDataCell>该账单的债权人地址</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">账单金额</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput placeholder="value" v-model="addBillValue"
                /></CTableDataCell>
                <CTableDataCell>该账单的金额</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">账单编号</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput placeholder="bid" v-model="addBillBid"
                /></CTableDataCell>
                <CTableDataCell>该账单的编号, 必须没有使用过</CTableDataCell>
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
                    v-on:click="addBill"
                    >交易</CButton
                  >
                </div></CCol
              >
              <CCol class="align-self-end"></CCol>
            </CRow>
          </CContainer>
          <br />
          <p>
            <font size="4" color="#3399ff"><strong>交易结果</strong></font>
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
                <CTableHeaderCell scope="row">交易状态</CTableHeaderCell>
                <CTableDataCell>{{ addBillStatus }}</CTableDataCell>
                <CTableDataCell>该账单的交易状态</CTableDataCell>
              </CTableRow>
            </CTableBody>
          </CTable>
        </CCardBody>
      </CCard>

      <CCard class="mb-4">
        <CCardHeader>
          <font size="5"><strong>分割-转让欠条</strong></font>
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
                <CTableHeaderCell scope="row">债权人地址</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="creditorAddress"
                    v-model="transferBillAddress"
                /></CTableDataCell>
                <CTableDataCell>该账单的债权人地址</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">债权人私钥</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="privkey"
                    v-model="transferBillPrivkey"
                /></CTableDataCell>
                <CTableDataCell>该账单的债权人私钥</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">新债权人地址</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="creditorAddress"
                    v-model="transferBillNewCreditor"
                /></CTableDataCell>
                <CTableDataCell>转让给的新债权人地址</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">新欠条金额</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="new value"
                    v-model="transferBillNewValue"
                /></CTableDataCell>
                <CTableDataCell>新欠条对应的欠款值金额</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">原账单编号</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="old bid"
                    v-model="transferBillOldBid"
                /></CTableDataCell>
                <CTableDataCell>原先账单的编号, 必须已存在</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">新账单编号</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="new bid"
                    v-model="transferBillNewBid"
                /></CTableDataCell>
                <CTableDataCell>新账单的编号, 必须没有使用过</CTableDataCell>
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
                    v-on:click="transferBill"
                    >交易</CButton
                  >
                </div></CCol
              >
              <CCol class="align-self-end"></CCol>
            </CRow>
          </CContainer>
          <br />
          <p>
            <font size="4" color="#3399ff"><strong>交易结果</strong></font>
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
                <CTableHeaderCell scope="row">交易状态</CTableHeaderCell>
                <CTableDataCell>{{ transferBillStatus }}</CTableDataCell>
                <CTableDataCell>该账单的交易状态</CTableDataCell>
              </CTableRow>
            </CTableBody>
          </CTable>
        </CCardBody>
      </CCard>

      <CCard class="mb-4">
        <CCardHeader>
          <font size="5"><strong>向金融机构融资</strong></font>
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
                <CTableHeaderCell scope="row">债务人地址</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="creditorAddress"
                    v-model="financeWithCreditAddress"
                /></CTableDataCell>
                <CTableDataCell>该账单的债权人地址</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">债权人私钥</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="privkey"
                    v-model="financeWithCreditPrivkey"
                /></CTableDataCell>
                <CTableDataCell>该账单的债务人私钥</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">金融公司地址</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="creditorAddress"
                    v-model="financeWithCreditCreditorAddress"
                /></CTableDataCell>
                <CTableDataCell>融资的金融公司地址</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">账单金额</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="new value"
                    v-model="financeWithCreditNewValue"
                /></CTableDataCell>
                <CTableDataCell>向金融公司融资的账单金额</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">账单编号</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="new bid"
                    v-model="financeWithCreditBid"
                /></CTableDataCell>
                <CTableDataCell>账单的编号, 必须没有使用过</CTableDataCell>
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
                    v-on:click="financeWithCredit"
                    >交易</CButton
                  >
                </div></CCol
              >
              <CCol class="align-self-end"></CCol>
            </CRow>
          </CContainer>
          <br />
          <p>
            <font size="4" color="#3399ff"><strong>交易结果</strong></font>
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
                <CTableHeaderCell scope="row">交易状态</CTableHeaderCell>
                <CTableDataCell>{{ financeWithCreditStatus }}</CTableDataCell>
                <CTableDataCell>该账单的交易状态</CTableDataCell>
              </CTableRow>
            </CTableBody>
          </CTable>
        </CCardBody>
      </CCard>

      <CCard class="mb-4">
        <CCardHeader>
          <font size="5"><strong>通过分割-转让欠条进行融资</strong></font>
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
                <CTableHeaderCell scope="row">债权人地址</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="creditorAddress"
                    v-model="financeWithBillTransferedAddress"
                /></CTableDataCell>
                <CTableDataCell>该账单的债权人地址</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">债权人私钥</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="privkey"
                    v-model="financeWithBillTransferedPrivkey"
                /></CTableDataCell>
                <CTableDataCell>该账单的债权人私钥</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">新债权人地址</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="newCreditorAddress"
                    v-model="financeWithBillTransferedCreditorAddress"
                /></CTableDataCell>
                <CTableDataCell>融资的新债权人地址</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">新欠条金额</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="new value"
                    v-model="financeWithBillTransferedNewValue"
                /></CTableDataCell>
                <CTableDataCell>新欠条对应的欠款值金额</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">原账单编号</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="old bid"
                    v-model="financeWithBillTransferedOldBid"
                /></CTableDataCell>
                <CTableDataCell>原先账单的编号, 必须已存在</CTableDataCell>
              </CTableRow>
              <CTableRow color="info">
                <CTableHeaderCell scope="row">新账单编号</CTableHeaderCell>
                <CTableDataCell
                  ><CFormInput
                    placeholder="new bid"
                    v-model="financeWithBillTransferedNewBid"
                /></CTableDataCell>
                <CTableDataCell>新账单的编号, 必须没有使用过</CTableDataCell>
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
                    v-on:click="financeWithBillTransfered"
                    >交易</CButton
                  >
                </div></CCol
              >
              <CCol class="align-self-end"></CCol>
            </CRow>
          </CContainer>
          <br />
          <p>
            <font size="4" color="#3399ff"><strong>交易结果</strong></font>
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
                <CTableHeaderCell scope="row">交易状态</CTableHeaderCell>
                <CTableDataCell>{{ 
                  financeWithBillTransferedStatus
                }}</CTableDataCell>
                <CTableDataCell>该账单的交易状态</CTableDataCell>
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
  name: 'Transaction',
  data() {
    return {
      addBillStatus: '',
      toasts: [],
      transferBillStatus: '',
      financeWithCreditStatus: '',
      financeWithBillTransferedStatus: '',
    }
  },
  methods: {
    success() {
      this.toasts.push({
        title: '交易成功',
        content: '交易结果已写入表格',
      })
    },
    fail() {
      this.toasts.push({
        title: '交易出错',
        content: '请输出正确的数据',
      })
    },
    addBill: function () {
      var that = this
      this.$http({
        method: 'post',
        url: 'api/bill/addBill',
        data: {
          address: this.addBillAddress,
          privkey: this.addBillPrivkey,
          creditor: this.addBillCreditor,
          value: this.addBillValue,
          bid: this.addBillBid,
        },
      })
        .then((res) => {
          if (res['data']['Status'] == -1) {
            this.addBillStatus = 'fail'
          } else {
            this.addBillStatus = 'success'
          }
          that.success()
        })
        .catch(function (error) {
          that.fail()
        })
    },
    transferBill: function () {
      var that = this
      this.$http({
        method: 'post',
        url: 'api/bill/transferBill',
        data: {
          address: this.transferBillAddress,
          privkey: this.transferBillPrivkey,
          new_creditor: this.transferBillCreditor,
          new_value: this.transferBillNewValue,
          old_id: this.transferBillOldBid,
          new_id: this.transferBillNewBid,
        },
      })
        .then((res) => {
          if (res['data']['Status'] == -1) {
            this.transferBillStatus = 'fail'
          } else {
            this.transferBillStatus = 'success'
          }
          that.success()
        })
        .catch(function (error) {
          that.fail()
        })
    },
    financeWithCredit: function () {
      var that = this
      this.$http({
        method: 'post',
        url: 'api/bill/financeWithCredit',
        data: {
          address: this.financeWithCreditAddress,
          privkey: this.financeWithCreditPrivkey,
          creditor_f: this.financeWithCreditCreditorAddress,
          fvalue: this.financeWithCreditNewValue,
          bid: this.financeWithCreditBid,
        },
      })
        .then((res) => {
          if (res['data']['Status'] == -1) {
            this.transferBillStatus = 'fail'
          } else {
            this.transferBillStatus = 'success'
          }
          that.success()
        })
        .catch(function (error) {
          that.fail()
        })
    },
    financeWithBillTransfered: function () {
      var that = this
      this.$http({
        method: 'post',
        url: 'api/bill/financeWithBillTransfered',
        data: {
          address: this.financeWithBillTransferedAddress,
          privkey: this.financeWithBillTransferedPrivkey,
          creditor_f: this.financeWithBillTransferedCreditorAddress,
          new_value: this.financeWithBillTransferedNewValue,
          old_id: this.financeWithBillTransferedOldBid,
          new_id: this.financeWithBillTransferedNewBid,
        },
      })
        .then((res) => {
          if (res['data']['Status'] == -1) {
            this.transferBillStatus = 'fail'
          } else {
            this.transferBillStatus = 'success'
          }
          that.success()
        })
        .catch(function (error) {
          that.fail()
        })
    },
  },
}
</script>
