<script setup>
import { reactive, ref } from 'vue'
import { message } from 'ant-design-vue'
import { loginAPI } from '@/api/accounts'
import { LoginOutlined } from '@ant-design/icons-vue'
import TaskiteLogo from '@/components/common/taskite-logo.vue'

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
  <a-flex class="flex justify-center items-center h-screen">
    <div>
      <div class="flex justify-center items-center mb-3 gap-2">
        <taskite-logo></taskite-logo>
        <div class="text-2xl font-bold">TasKite Cloud</div>
      </div>
      <a-card class="px-2 py-1 w-96">
        <a-flex justify="center">
          <p class="text-2xl font-medium">Log in</p>
        </a-flex>
        <a-form :model="loginForm" layout="vertical" @finish="handleLogin" hideRequiredMark>
          <a-form-item label="Email" name="email" :rules="[{ required: true, message: 'Please input your email!' }]">
            <a-input v-model:value="loginForm.email" />
          </a-form-item>
          <a-form-item label="Password" name="password"
            :rules="[{ required: true, message: 'Please input your password!' }]">
            <a-input-password v-model:value="loginForm.password" />
          </a-form-item>
          <a-form-item>
            <a-button :loading="loading" type="primary" html-type="submit" class="w-full">
              Login
              <template #icon>
                <LoginOutlined />
              </template>
            </a-button>
          </a-form-item>
        </a-form>
        <div class="flex justify-center">
          <p>Don't have an account ? <a class="hover:underline" href="/accounts/register/">Create an account</a></p>
        </div>
        <!-- <hr class="border border-dashed h-px border-gray-400"> -->
        <div class="flex justify-center">
          <a href="">
            <p class="text-gray-500 hover:underline">Forgot password ?</p>
          </a>
        </div>
      </a-card>
    </div>
  </a-flex>
</template>

<style scoped>
</style>
