<script setup>
import axios from 'axios'
import { reactive } from 'vue'
import { message } from 'ant-design-vue'
import { loginAPI } from '@/utils/api'

const props = defineProps(['next'])
const loginForm = reactive({
  email: '',
  password: '',
})

const handleLogin = async (values) => {
  try {
    await loginAPI(values)
    window.location.href = props.next
  } catch (error) {
    message.warning(error.response.data.detail)
  }
}
</script>

<template>
  <a-flex justify="center" align="center" style="height: 100vh">
    <a-card>
      <a-form :model="loginForm" layout="vertical" @finish="handleLogin">
        <a-form-item label="Email" name="email">
          <a-input v-model:value="loginForm.email" />
        </a-form-item>
        <a-form-item label="Password" name="password">
          <a-input-password v-model:value="loginForm.password" />
        </a-form-item>
        <a-form-item>
          <a-button type="primary" html-type="submit">Login</a-button>
        </a-form-item>
      </a-form>
    </a-card>
  </a-flex>
</template>
