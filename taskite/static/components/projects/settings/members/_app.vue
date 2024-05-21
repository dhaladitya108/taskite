<script setup>
import { ref, onMounted, computed } from 'vue'

import ProjectSettingsLayout from '@/components/layouts/project-settings-layout.vue'
import MemberAddForm from '@/components/projects/settings/members/member-add-form.vue'
import { projectMembersListAPI, projectMemberUpdateAPI, projectInviteListAPI } from '@/utils/api'
import { generateAvatar } from '@/utils/generators'
import {
  ProjectOutlined,
  UserSwitchOutlined,
  ExpandAltOutlined,
  DeleteOutlined,
} from '@ant-design/icons-vue'
import { message } from 'ant-design-vue'

const props = defineProps(['project', 'role'])

const projectMembers = ref([])
const projectInvites = ref([])

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
    message.error('Failed to fetch project members!')
  }
}

const fetchProjectInvites = async () => {
  try {
    const { data } = await projectInviteListAPI(props.project.id)
    projectInvites.value = data
  } catch (error) {
    console.log(error)
  }
}

const updateProjectMember = async (projectMemberId, updatedData) => {
  try {
    await projectMemberUpdateAPI(props.project.id, projectMemberId, updatedData)
    message.success('Member detail updated!')
  } catch (error) {
    message.error('Failed to update project member details!')
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
  {
    name: 'Action',
    key: 'action',
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
  fetchProjectInvites()
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
            <a href="/projects">
              <project-outlined></project-outlined>
              <span>Projects</span>
            </a>
          </a-breadcrumb-item>
          <a-breadcrumb-item><a :href="`/${props.project.slug}/`">{{ props.project.name }}</a></a-breadcrumb-item>
          <a-breadcrumb-item>
            <a :href="`/${props.project.slug}/settings/general/`">
              <user-switch-outlined></user-switch-outlined>
              <span style="margin-left: 4px">General</span>
            </a>
          </a-breadcrumb-item>
        </a-breadcrumb>
      </div>

      <div>
        <a-button type="primary" @click="() => (showMemberInviteModal = true)">+ Invite Member</a-button>
        <a-dropdown v-show="projectInvites.length > 0">
          <a-badge :count="projectInvites.length">
            <a-button type="dashed" class="ml-2">Pending Invitations</a-button>
          </a-badge>

          <template #overlay>
            <a-card size="small">
              <div v-for="projectInvite in projectInvites" :key="projectInvite.id">{{ projectInvite.email }} <a-button type="link">Delete</a-button></div>
            </a-card>
            </template>
        </a-dropdown>
        <a-modal v-model:open="showMemberInviteModal" :footer="null">
          <member-add-form :projectId="props.project.id" @memberInvited="() => fetchProjectInvites()"></member-add-form>
        </a-modal>
      </div>
    </a-flex>
    <a-flex gap="middle" justify="end"> </a-flex>
    <a-table :columns="tableColumns" :data-source="projectMembers">
      <template #bodyCell="{ column, record }">
        <template v-if="column.key == 'username'"><a-avatar size="small" :src="getAvatar(record.user)"> </a-avatar>
          {{ record.user.username }}
        </template>

        <template v-if="column.key == 'name'">
          {{ record.user.fullName }}
        </template>

        <template v-if="column.key == 'email'">
          {{ record.user.email }}
        </template>

        <template v-if="column.key == 'role'">
          <div v-if="record.joinedAt == null">
            <a-button>
              <template #icon>
                <ExpandAltOutlined />
              </template>
              Invited
            </a-button>
          </div>
          <div v-else>
            <a-select ref="select" v-model:value="record.role" style="width: 120px"
              @change="(value) => handleRoleChange(record.id, value)" :disabled="props.role !== 'admin'">
              <a-select-option value="admin">Admin</a-select-option>
              <a-select-option value="member">Member</a-select-option>
              <a-select-option value="guest">Guest</a-select-option>
            </a-select>
          </div>
        </template>

        <template v-if="column.key == 'action'">
          <a-button>
            <template #icon>
              <DeleteOutlined />
            </template>
          </a-button>
        </template>
      </template>
    </a-table>
  </ProjectSettingsLayout>
</template>
