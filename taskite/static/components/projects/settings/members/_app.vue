<script setup>
import { ref, onMounted, computed } from 'vue'

import ProjectSettingsLayout from '@/components/layouts/project-settings-layout.vue'
import { projectMembersListAPI, projectMemberUpdateAPI } from '@/utils/api'
import { generateAvatar } from '@/utils/generators'

const props = defineProps(['projectSlug', 'projectId'])

const projectMembers = ref([])

const fetchMembers = async () => {
  try {
    const { data } = await projectMembersListAPI(props.projectId)
    projectMembers.value = data.map((member) => {
      return {
        key: member.id,
        ...member,
      }
    })
  } catch (error) {
    console.log(error)
  }
}

const updateProjectMember = async (projectMemberId, updatedData) => {
  try {
    await projectMemberUpdateAPI(props.projectId, projectMemberId, updatedData)
  } catch (error) {
    console.log
  }
}

const tableColumns = [
  {
    title: 'Username',
    name: 'Username',
    key: 'username',
  },
  {
    title: 'Name',
    name: 'Name',
    key: 'name',
  },
  {
    title: 'Email',
    name: 'Email',
    key: 'email',
  },
  {
    title: 'Role',
    name: 'Role',
    key: 'role',
  },
]

// const tableRows = computed(() => {
//   return projectMembers.value.map((member) => {
//     return {
//       ...member,
//       key: user.id,
//     }
//   })
// })

const handleRoleChange = (projectMemberId, role) => {
  const updatedData = {
    role: role,
  }
  updateProjectMember(projectMemberId, updatedData)
}

onMounted(() => {
  fetchMembers()
})
</script>

<template>
  <ProjectSettingsLayout page="members" :projectSlug="props.projectSlug">
    <h1>Members</h1>
    <a-table :columns="tableColumns" :data-source="projectMembers">
      <template #bodyCell="{ column, record }">
        <template v-if="column.key == 'username'"
          ><a-avatar size="small" :src="generateAvatar(record.user.fullName)">
          </a-avatar>
          {{ record.user.username }}
        </template>

        <template v-if="column.key == 'name'">
          {{ record.user.fullName }}
        </template>

        <template v-if="column.key == 'email'">
          {{ record.user.email }}
        </template>

        <template v-if="column.key == 'role'">
          <a-select
            ref="select"
            v-model:value="record.role"
            style="width: 120px"
            @change="(value) => handleRoleChange(record.id, value)"
          >
            <a-select-option value="admin">Admin</a-select-option>
            <a-select-option value="member">Member</a-select-option>
            <a-select-option value="guest">Guest</a-select-option>
          </a-select>
        </template>
      </template>
    </a-table>
  </ProjectSettingsLayout>
</template>
