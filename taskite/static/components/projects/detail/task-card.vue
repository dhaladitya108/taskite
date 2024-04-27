<script setup>
import TaskDetailCard from '@/components/projects/detail/task-detail-card.vue';

import { ref, computed } from 'vue'
import { generateAvatar } from '@/utils/generators'

const { task, project } = defineProps(['task', 'project'])

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

const show_task_modal = ref(false)
function open_task_modal() {
  show_task_modal.value = true
}
</script>

<template>
  <a-card id="task-card" size="small" @click="open_task_modal">
    <a-flex justify="space-between">
      <div>
        <a-typography-text type="secondary" style="font-size: smaller">{{
          task.task_id
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
          :title="assignee.display_name"
          placement="top"
          v-for="assignee in task.assignees"
          :key="assignee.id"
        >
          <a-avatar size="small" :src="generateAvatar(assignee.full_name)"> </a-avatar>
        </a-tooltip>
      </a-avatar-group>
    </a-flex>
  </a-card>

  <a-modal v-model:open="show_task_modal" width="700px" :footer="null">
    <task-detail-card :task="task" :project="project"></task-detail-card>
  </a-modal>
</template>

<style scoped>
#task-card {
  width: 320px;
}
</style>
