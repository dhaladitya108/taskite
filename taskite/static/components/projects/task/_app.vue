<script setup>
import DashboardLayout from '@/components/dashboard-layout.vue'
import TaskDetailModal from '@/components/projects/detail/task-detail-modal.vue'

const props = defineProps(['project', 'task_id'])
</script>

<template>
  <dashboard-layout>
    <task-detail-modal
      :projectId="props.project.id"
      :taskId="props.task_id"
      :projectSlug="props.project.slug"
      :projectName="props.project.name"
    ></task-detail-modal>
  </dashboard-layout>
</template>
