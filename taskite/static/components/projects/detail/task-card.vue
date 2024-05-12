<script setup>
import { ref, computed } from 'vue'
import { generateAvatar } from '@/utils/generators'

import TaskDetailModal from '@/components/projects/detail/task-detail-modal.vue'

const { task, project, members } = defineProps(['task', 'project', 'members'])
const emit = defineEmits(['updated'])

const priorityTagColor = computed(() => {
  switch (task.priority) {
    case 'urgent':
      return 'red'

    case 'high':
      return 'orange'

    case 'medium':
      return 'blue'

    case 'low':
      return 'secondary'

    default:
      return ''
  }
})

const showTaskDetailModal = ref(false)
function openTaskDetailModal() {
  showTaskDetailModal.value = true
}

const handleTaskUpdateFromModal = (payload) => {
  emit('updated', payload)

  Object.keys(payload).forEach((key) => {
    task[key] = payload[key]
  })
}

const getAvatar = (record) => {
  if (!record.avatar) {
    return generateAvatar(record.fullName)
  }

  return record.avatar
}

const getPriorityCardColor = computed(() => {
  switch (task.priority) {
    case 'urgent':
      return '#fff2f2'

    case 'high':
      return '#ffecde'

    case 'medium':
      return '#deefff'

    case 'low':
      return '#cccccc'

    default:
      return ''
  }
})
</script>

<template>
  <a-card
    id="task-card"
    size="small"
    @click="openTaskDetailModal"
  >
    <a-flex justify="space-between">
      <div>
        <a-typography-text type="secondary" style="font-size: smaller">{{
          task.taskId
        }}</a-typography-text>
      </div>
      <a-tag :color="priorityTagColor" :bordered="false">
        <a-typography-text style="font-size: smaller">
          {{ task.priority }}
        </a-typography-text>
      </a-tag>
    </a-flex>
    <div>{{ task.name }}</div>
    <a-flex justify="end">
      <a-avatar-group>
        <a-tooltip
          :title="assignee.displayName"
          placement="top"
          v-for="assignee in task.assignees"
          :key="assignee.id"
        >
          <a-avatar size="small" :src="getAvatar(assignee)"> </a-avatar>
        </a-tooltip>
      </a-avatar-group>
    </a-flex>
  </a-card>

  <a-modal
    v-model:open="showTaskDetailModal"
    width="1000px"
    :footer="null"
    :destroyOnClose="true"
  >
    <task-detail-modal
      :taskId="task.id"
      :projectId="project.id"
      :projectSlug="project.slug"
      :projectName="project.name"
      :members="members"
      @updated="handleTaskUpdateFromModal"
    ></task-detail-modal>
  </a-modal>
</template>

<style scoped>
#task-card {
  width: 320px;
}
</style>
