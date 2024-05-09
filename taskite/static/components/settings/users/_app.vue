<script setup>
import { ref, onMounted, computed } from 'vue'

import DashboardLayout from '@/components/layouts/dashboard-layout.vue'
import { userListAPI } from '@/utils/api'
import { generateAvatar } from '@/utils/generators'

const users = ref([])

const tableColumns = [
  {
    title: 'Name',
    name: 'Name',
    dataIndex: 'fullName',
    key: 'fullName',
  },
  {
    title: 'Username',
    name: 'Username',
    dataIndex: 'username',
    key: 'username',
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

const getAvatar = (record) => {
  if (!record.avatar) {
    return generateAvatar(record.fullName)
  }

  return record.avatar
}
</script>

<template>
  <dashboard-layout>
    <div class="tk-main-content" id="users-page">
      <a-flex justify="center">
        <a-table :columns="tableColumns" :data-source="tableRows">
          <template #bodyCell="{ column, record }">
            <template v-if="column.key == 'fullName'"
              ><a-avatar size="small" :src="getAvatar(record)"> </a-avatar>
              {{ record.fullName }}
            </template>
          </template>
        </a-table>
      </a-flex>
    </div>
  </dashboard-layout>
</template>

<style scoped>
  #users-page {
    margin-top: 50px;
  }
</style>
