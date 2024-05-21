<script setup>
import { reactive, ref } from 'vue'
import { message } from 'ant-design-vue'
import { loginAPI } from '@/utils/api'
import { LoginOutlined } from '@ant-design/icons-vue'

const props = defineProps(['next'])
const loginForm = reactive({
  email: '',
  password: '',
})
const loading = ref(false)

const handleLogin = async (values) => {
  try {
    loading.value = true
    await loginAPI(values)
    window.location.href = props.next
  } catch (error) {
    message.warning(error.response.data.detail)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <a-flex justify="center" align="center" style="height: 100vh">
    <a-card id="login-card">
      <a-flex justify="center">
        <a-typography-title :level="3">Log In</a-typography-title>
      </a-flex>
      <a-form :model="loginForm" layout="vertical" @finish="handleLogin">
        <a-form-item label="Email" name="email" :rules="[{ required: true, message: 'Please input your email!' }]">
          <a-input v-model:value="loginForm.email" />
        </a-form-item>
        <a-form-item label="Password" name="password"
          :rules="[{ required: true, message: 'Please input your password!' }]">
          <a-input-password v-model:value="loginForm.password" />
        </a-form-item>
        <a-form-item>
          <a-button :loading="loading" type="primary" html-type="submit">
            Login
            <template #icon>
              <LoginOutlined />
            </template>
          </a-button>
        </a-form-item>
      </a-form>
    </a-card>
  </a-flex>
</template>

<style scoped>
#login-card {
  width: 25%;
  -webkit-box-shadow: 0px 0px 14px 15px rgba(237, 237, 237, 1);
  -moz-box-shadow: 0px 0px 14px 15px rgba(237, 237, 237, 1);
  box-shadow: 0px 0px 14px 15px rgba(237, 237, 237, 1);
}
</style>
