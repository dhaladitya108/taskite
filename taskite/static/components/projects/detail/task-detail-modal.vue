<script setup>
import { ref } from 'vue'
import { onMounted } from 'vue'
import { taskDetailAPI } from '@/utils/api'

import LoadingSpinner from '@/components/common/loading-spinner.vue'

const props = defineProps(['taskId', 'projectId'])
const task = ref(null)

const fetchTaskDetail = async () => {
  try {
    const { data } = await taskDetailAPI(props.projectId, props.taskId)
    task.value = data
  } catch (error) {
    console.log(error)
  }
}
onMounted(async () => {
  fetchTaskDetail()
})
</script>

<template>
  <div v-if="!!task">
    <a-breadcrumb>
      <a-breadcrumb-item>Project</a-breadcrumb-item>
      <a-breadcrumb-item>
        <a :href="`${task.taskId}`">{{ task.taskId }}</a>
      </a-breadcrumb-item>
    </a-breadcrumb>
    
  </div>
  <div v-else>
    <a-flex justify="center" align="center" style="height: 40vh">
        <loading-spinner />
    </a-flex>
    </div>
</template>
