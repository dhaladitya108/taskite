<script setup>
import { reactive, ref } from 'vue'
import { projectMemberInviteAPI } from '@/utils/api'
import { message } from 'ant-design-vue'

const props = defineProps(['projectId'])
const emit = defineEmits(['memberInvited'])

const memberRoleChoices = [
  {
    label: 'Member',
    value: 'member',
  },
  {
    label: 'Admin',
    value: 'admin',
  },
  {
    label: 'Guest',
    value: 'guest',
  },
]

const inviteForm = ref({
  emails: '',
  message: '',
  role: 'member',
})
const loading = ref(false)

const submitForm = async (values) => {
  const data = {
    ...values,
    emails: values.emails.split(',').map(email => email.toLowerCase().trim()),
  }

  loading.value = true

  try {
    await projectMemberInviteAPI(props.projectId, data)
    emit('memberInvited')
  } catch (error) {
    message.error('Failed to invite members')
  } finally {
    loading.value = false

    // Resetting the form
    inviteForm.value.emails = []
    inviteForm.value.role = "member"
  }
}
</script>

<template>
  <h2>Invite Members</h2>
  <a-form layout="vertical" :model="inviteForm" @finish="submitForm">
    <a-form-item label="Emails" name="emails" :rules="[{ required: true, message: 'Please enter invitees email!' }]"
      extra="For multiple emails, please enter emails with comma separated">
      <a-textarea v-model:value="inviteForm.emails" :rows="2"></a-textarea>
    </a-form-item>
    <a-form-item label="Role" name="role">
      <a-select :options="memberRoleChoices" v-model:value="inviteForm.role"></a-select>
    </a-form-item>
    <a-form-item label="Message" name="message">
      <a-textarea v-model:value="inviteForm.message" :rows="4"></a-textarea>
    </a-form-item>
    <a-form-item>
      <a-button html-type="submit" type="primary" :loading>Invite</a-button>
    </a-form-item>
  </a-form>
</template>

<style scoped></style>
