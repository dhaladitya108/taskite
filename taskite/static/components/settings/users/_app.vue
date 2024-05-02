<script setup>
import { ref, onMounted, computed } from 'vue'

import DashboardLayout from '@/components/layouts/dashboard-layout.vue'
import { userListAPI } from '@/utils/api'
import { generateAvatar } from '@/utils/generators'

const users = ref([])

const tableColumns = [
  {
    // title: 'Username',
    name: 'Username',
    dataIndex: 'username',
    key: 'username',
  },
  {
    title: 'Name',
    name: 'Name',
    dataIndex: 'fullName',
    key: 'fullName',
  },
  {
    title: 'Email',
    name: 'Email',
    dataIndex: 'email',
    key: 'email',
  },
  {
    title: 'Role',
    name: 'Role',
    dataIndex: 'role',
    key: 'role',
  },
]

const tableRows = computed(() => {
  return users.value.map((user) => {
    return {
      ...user,
      key: user.id,
    }
  })
})

const fetchUsers = async () => {
  try {
    const { data } = await userListAPI()
    users.value = data
  } catch (error) {
    console.log(error)
  }
}

onMounted(() => {
  fetchUsers()
})
</script>

<template>
  <dashboard-layout>
    <div class="tk-main-content">
      <h1>Users</h1>
      <a-table :columns="tableColumns" :data-source="tableRows">
        <template #bodyCell="{ column, record }">
          <template v-if="column.key == 'username'"
            ><a-avatar size="small" :src="generateAvatar(record.fullName)">
            </a-avatar>
            {{ record.username }}
          </template>
        </template>
      </a-table>
    </div>
  </dashboard-layout>
</template>
