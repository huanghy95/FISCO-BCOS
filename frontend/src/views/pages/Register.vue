<template>
  <div class="bg-light min-vh-100 d-flex flex-row align-items-center">
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
    <CModal
      alignment="center"
      :visible="visibleVerticallyCenteredDemo"
      @close="
        () => {
          visibleVerticallyCenteredDemo = false
        }
      "
      size="lg"
    >
      <CModalHeader>
        <CModalTitle>注册成功</CModalTitle>
      </CModalHeader>
      <CModalBody>
        <p>
          <font size="4" color="#3399ff"><strong>请保存好账户信息</strong></font>
          <br />
        </p>
        <CTable>
          <CTableHead color="secondary">
            <CTableRow>
              <CTableHeaderCell scope="col" style="width: 200px"
                >属性</CTableHeaderCell
              >
              <CTableHeaderCell scope="col">输出</CTableHeaderCell>
            </CTableRow>
          </CTableHead>
          <CTableBody>
            <CTableRow color="info">
              <CTableHeaderCell scope="row">地址</CTableHeaderCell>
              <CTableDataCell>{{ address }}</CTableDataCell>
            </CTableRow>
            <CTableRow color="info">
              <CTableHeaderCell scope="row">私钥</CTableHeaderCell>
              <CTableDataCell>{{ privkey }}</CTableDataCell>
            </CTableRow>
            <CTableRow color="info">
              <CTableHeaderCell scope="row">公钥</CTableHeaderCell>
              <CTableDataCell>{{ pubkey }}</CTableDataCell>
            </CTableRow>
          </CTableBody>
        </CTable>
      </CModalBody>
      <CModalFooter>
        <CButton
          color="secondary"
          @click="
            () => {
              visibleVerticallyCenteredDemo = false
            }
          "
        >
          确定
        </CButton>
      </CModalFooter>
    </CModal>

    <CContainer>
      <CRow class="justify-content-center">
        <CCol :md="9" :lg="7" :xl="6">
          <CCard class="mx-4">
            <CCardBody class="p-4">
              <CForm class="text-center">
                <h1>账户注册</h1>
                <p class="text-medium-emphasis">输入用户名, 密码以及账户类型</p>
                <CInputGroup class="mb-3">
                  <CInputGroupText>
                    <CIcon icon="cil-user" />
                  </CInputGroupText>
                  <CFormInput
                    placeholder="Username"
                    autocomplete="username"
                    v-model="username"
                  />
                </CInputGroup>
                <CInputGroup class="mb-3">
                  <CInputGroupText>
                    <CIcon icon="cil-user" />
                  </CInputGroupText>
                  <CFormInput
                    type="acctype"
                    placeholder="Account type(str): Company or Finance"
                    autocomplete="account type"
                    v-model="acctype"
                  />
                </CInputGroup>
                <CInputGroup class="mb-3">
                  <CInputGroupText>
                    <CIcon icon="cil-lock-locked" />
                  </CInputGroupText>
                  <CFormInput
                    type="password"
                    placeholder="Password"
                    autocomplete="new-password"
                    v-model="password"
                  />
                </CInputGroup>
                <CInputGroup class="mb-3">
                  <CInputGroupText>
                    <CIcon icon="cilMoney" />
                  </CInputGroupText>
                  <CFormInput
                    type="value"
                    placeholder="Value(int)"
                    v-model="value"
                  />
                </CInputGroup>
                <div class="d-grid">
                  <CButton color="info" v-on:click="register">注册账户</CButton>
                </div>

                <div class="d-grid" style="padding-top: 10px">
                  <CButton color="dark" v-on:click="back">返回</CButton>
                </div>
              </CForm>
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
    </CContainer>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return {
      address: '',
      privkey: '',
      pubkey: '',
      toasts: [],
      visibleVerticallyCenteredDemo: false,
    }
  },
  methods: {
    fail() {
      this.toasts.push({
        title: '注册失败',
        content: '请输入正确格式的数据',
      })
    },
    formData: function () {
      var value
      if (this.value == 'Company') {
        value = 0
      } else if (this.value == 'Finance') {
        value = 1
      } else value = this.value
      return {
        username: this.username,
        password: this.password,
        acctype: this.acctype,
        value: value,
      }
    },
    register: function () {
      var that = this
      this.$http({
        method: 'post',
        url: 'api/account/register',
        data: this.formData(),
      })
        .then((res) => {
          that.visibleVerticallyCenteredDemo = true
          that.address = res['data']['Address']
          that.privkey = res['data']['Privkey']
          that.pubkey = res['data']['Pubkey']
          that.pubkey = that.pubkey.slice(0, 63) + '\n' + that.pubkey.slice(63)
        })
        .catch(function (error) {
          that.fail()
        })
    },
    back: function () {
      this.$router.push({
        path: '/dashboard',
      })
    },
  },
}
</script>
