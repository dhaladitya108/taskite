<script setup>
import { reactive, ref } from 'vue'
import { message } from 'ant-design-vue'
import { registerAPI } from '@/api/accounts'
import { CloudServerOutlined } from '@ant-design/icons-vue'

const registerForm = reactive({
    fullName: '',
    email: '',
    password: '',
})
const loading = ref(false)

const handleLogin = async (values) => {
    try {
        loading.value = true
        await registerAPI(values)
        window.location.href = "/"
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
            <div class="flex justify-center">
                <p class="text-2xl font-bold">TasKite Cloud</p>
            </div>
            <a-card class="px-2 py-1 w-96">
                <a-flex justify="center">
                    <p class="text-2xl font-medium">Get started</p>
                </a-flex>
                <a-form :model="registerForm" layout="vertical" @finish="handleLogin" hideRequiredMark>
                    <a-form-item label="Name" name="fullName"
                        :rules="[{ required: true, message: 'Please input your name!' }]">
                        <a-input v-model:value="registerForm.fullName" />
                    </a-form-item>
                    <a-form-item label="Email" name="email"
                        :rules="[{ required: true, message: 'Please input your email!' }]">
                        <a-input v-model:value="registerForm.email" />
                    </a-form-item>
                    <a-form-item label="Password" name="password"
                        :rules="[{ required: true, message: 'Please input your password!' }]">
                        <a-input-password v-model:value="registerForm.password" />
                    </a-form-item>
                    <a-form-item>
                        <a-button :loading="loading" type="primary" html-type="submit" class="w-full">
                            Register
                            <template #icon>
                                <cloud-server-outlined />
                            </template>
                        </a-button>
                    </a-form-item>
                </a-form>
                <div class="flex justify-center">
                    <p>Already have an account ? <a class="hover:underline" href="/accounts/login/">Login</a></p>
                </div>
            </a-card>
        </div>
    </a-flex>
</template>

<style scoped></style>
