<script setup>
import { ref, computed } from 'vue'
import { generateAvatar } from '@/utils/generators'

const { task, project } = defineProps(['task', 'project'])
const emit = defineEmits(['selected'])

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

function open_task_modal() {
  emit('selected', task.id)
}
</script>

<template>
  <a-card id="task-card" size="small" @click="open_task_modal">
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
          <a-avatar size="small" :src="generateAvatar(assignee.fullName)"> </a-avatar>
        </a-tooltip>
      </a-avatar-group>
    </a-flex>
  </a-card>
</template>

<style scoped>
#task-card {
  width: 320px;
}
</style>
