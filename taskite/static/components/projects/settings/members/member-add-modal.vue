<script setup>
import { reactive, ref } from 'vue'
import { MinusCircleOutlined, PlusOutlined } from '@ant-design/icons-vue'

const memberInviteForm = reactive({
  emails: [],
  role: '',
  message: '',
})
const formRef = ref()

const removeEmail = (email) => {
  console.log(email)
}
const addEmail = () => {
  memberInviteForm.emails.push('')
}
</script>

<template>
  <a-form :model="memberInviteForm" ref="formRef">
    <a-form-item
      v-for="email in memberInviteForm"
      :key="email"
      :name="emails"
    >
      <a-input
        v-model:value="email.value"
        placeholder="please input email"
        style="width: 60%; margin-right: 8px"
      />
      <MinusCircleOutlined
        v-if="memberInviteForm.emails.length > 1"
        class="dynamic-delete-button"
        @click="removeEmail(email)"
      />
    </a-form-item>
    <a-form-item>
      <a-button type="dashed" style="width: 60%" @click="addEmail">
        <PlusOutlined />
        Add field
      </a-button>
    </a-form-item>
  </a-form>
</template>

<style scoped>
.dynamic-delete-button {
  cursor: pointer;
  position: relative;
  top: 4px;
  font-size: 24px;
  color: #999;
  transition: all 0.3s;
}
.dynamic-delete-button:hover {
  color: #777;
}
.dynamic-delete-button[disabled] {
  cursor: not-allowed;
  opacity: 0.5;
}
</style>
