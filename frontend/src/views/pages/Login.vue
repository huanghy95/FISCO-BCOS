<template>
  <div class="bg-light min-vh-100 d-flex flex-row align-items-center" style="padding-bottom: 50px;">
    <CContainer>
      <CRow class="justify-content-center">
        <CCol :md="7">
            <CCard color="dark" class="text-white bg-primary py-5" style="width: 100%" >
              <CCardBody class="text-center">
                <div>
                  <h2>欢迎来到基于区块链的供应链金融平台!</h2>
                </div>
                <div>
                  <CButton color="light" variant="outline" class="mt-3" v-on:click="enter">
                    进入系统
                  </CButton>
                </div>
              </CCardBody>
            </CCard>
        </CCol>
      </CRow>
    </CContainer>
  </div>
</template>

<script>
export default {
  name: 'Login',
  methods: {
    formData:function(){
        return{
            "username":this.username,
            "password": this.password,
            "acctype": "Company",
            "value": 0
    }},
    login:function() {
      this.$http({
      method:'post',
      url:'api/account/register',
      data:this.formData()
    }).then(res=>{
      console.log(res)
    })
    },
    enter:function(){
        this.$router.push({
        path: '/dashboard',
        })
    }
}
}
</script>
