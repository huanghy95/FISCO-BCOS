<template>
  <CDropdown variant="nav-item">
    <CDropdownToggle placement="bottom-end" class="py-0" :caret="false">
      <CAvatar :src="avatar" size="md" />
    </CDropdownToggle>
    <CDropdownMenu class="pt-0">
      <CDropdownHeader component="h6" class="bg-light fw-semibold py-2">
        账户
      </CDropdownHeader>
      <CDropdownItem  class="text-center"> 
        <CButton color="light" v-on:click="register" shape="rounded-0" style="width:150px;">  账户注册  </CButton>
      </CDropdownItem>
    </CDropdownMenu>
  </CDropdown>
</template>

<script>
import avatar from '@/assets/images/avatars/user.png'
export default {
  name: 'AppHeaderDropdownAccnt',
  setup() {
    return {
      avatar: avatar,
    }
  },
  methods: {
    register:function(){
        this.$router.push({
        path: '/pages/register',
        })
    }
}
}
</script>
