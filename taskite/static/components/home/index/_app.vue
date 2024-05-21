<script setup>
import { onMounted, ref } from 'vue'
import { DownOutlined } from '@ant-design/icons-vue'

import DashboardLayout from '@/components/layouts/dashboard-layout.vue'
import { projectInvitesAPI } from '@/utils/api'

const props = defineProps(['user'])

const invites = ref([])

const fetchProjectInvites = async () => {
  try {
    const { data } = await projectInvitesAPI()
    console.log(data)
    invites.value = data
  } catch (error) {
    console.log(error)
  }
}

onMounted(async () => {
  fetchProjectInvites()
})
</script>

<template>
  <dashboard-layout page="home">
    <div class="container mx-auto px-6 py-6">
      <div class="flex flex-row justify-between">
        <p class="text-xl">Hi. {{ props.user.fullName }}</p>
        <div>
          <a-dropdown>
            <a class="ant-dropdown-link" @click.prevent>
              <a-badge :count="invites.length">
                <a-button :disabled="invites.length === 0" type="dashed">Invitations</a-button>
              </a-badge>
            </a>
            <template #overlay>
              <div>
                <div v-for="invite in invites" class="flex flex-row items-center">
                  <div>{{ invite.project.name }}</div>
                  <div class="flex flex-row">
                    <a-button type="link"><a :href="`/projects/invite/${invite.id}/confirm/`">Accept</a></a-button>
                    <a-button type="link" danger><a
                        :href="`/projects/invite/${invite.id}/reject/`">Reject</a></a-button>
                  </div>
                </div>
              </div>
            </template>
          </a-dropdown>
        </div>
      </div>
    </div>
  </dashboard-layout>
</template>
