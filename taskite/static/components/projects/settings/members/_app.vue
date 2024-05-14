<script setup>
import { ref, onMounted, computed } from 'vue'

import ProjectSettingsLayout from '@/components/layouts/project-settings-layout.vue'
import MemberAddModal from '@/components/projects/settings/members/member-add-modal.vue'
import { projectMembersListAPI, projectMemberUpdateAPI } from '@/utils/api'
import { generateAvatar } from '@/utils/generators'
import { ProjectOutlined, UserSwitchOutlined } from '@ant-design/icons-vue'

const props = defineProps(['project', 'role'])

const projectMembers = ref([])

const fetchMembers = async () => {
  try {
    const { data } = await projectMembersListAPI(props.project.id)
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
    await projectMemberUpdateAPI(props.project.id, projectMemberId, updatedData)
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

const handleRoleChange = (projectMemberId, role) => {
  const updatedData = {
    role: role,
  }
  updateProjectMember(projectMemberId, updatedData)
}

onMounted(() => {
  fetchMembers()
})

const showMemberInviteModal = ref(false)

const getAvatar = (record) => {
  if (!record.avatar) {
    return generateAvatar(record.fullName)
  }

  return record.avatar
}
</script>

<template>
  <ProjectSettingsLayout page="members" :projectSlug="props.project.slug" :themeColor="props.project.themeColor">
    <a-flex justify="space-between">
      <div class="tk-breadcrump">
        <a-breadcrumb>
          <a-breadcrumb-item>
            <project-outlined></project-outlined>
            <span>Projects</span>
          </a-breadcrumb-item>
          <a-breadcrumb-item
            ><a :href="`/${props.project.slug}/`">{{
              props.project.name
            }}</a></a-breadcrumb-item
          >
          <a-breadcrumb-item>
            <a :href="`/${props.project.slug}/settings/general/`">
              <user-switch-outlined></user-switch-outlined>
              <span style="margin-left: 4px">General</span>
            </a>
          </a-breadcrumb-item>
        </a-breadcrumb>
      </div>

      <a-button type="primary" @click="() => (showMemberInviteModal = true)"
        >+ Invite Member</a-button
      >
      <a-modal v-model:open="showMemberInviteModal">
        <member-add-modal></member-add-modal>
      </a-modal>
    </a-flex>
    <a-flex gap="middle" justify="end"> </a-flex>
    <a-table :columns="tableColumns" :data-source="projectMembers">
      <template #bodyCell="{ column, record }">
        <template v-if="column.key == 'username'"
          ><a-avatar size="small" :src="getAvatar(record.user)"> </a-avatar>
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
            :disabled="props.role !== 'admin'"
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
