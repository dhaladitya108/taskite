<script setup>
import { computed } from 'vue'
import { createAvatar } from '@dicebear/core'
import { initials } from '@dicebear/collection'

const avatar = (seed) =>
  createAvatar(initials, {
    seed: seed,
    backgroundColor: ['1677ff'],
    // ... other options
  }).toDataUriSync()

const { task } = defineProps(['task'])

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
</script>

<template>
  <a-card style="width: 265px" size="small">
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
          <a-avatar size="small" :src="avatar(assignee.full_name)"> </a-avatar>
        </a-tooltip>
      </a-avatar-group>
    </a-flex>
  </a-card>
</template>

<style scoped></style>
