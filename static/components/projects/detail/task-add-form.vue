<script setup>
import { reactive } from 'vue'
import { message } from 'ant-design-vue'

import { taskAddAPI } from '@/utils/api'
const props = defineProps(['projectId', 'stateId'])
const emit = defineEmits(['newTaskAdded'])

const task_form = reactive({
  name: '',
})

const onFinish = async (values) => {
  values['stateId'] = props.stateId

  try {
    const { data } = await taskAddAPI(props.projectId, values)
    message.success(data.detail)

    emit('newTaskAdded', props.stateId, data.task)
  } catch (error) {
    console.log(error)
  }
}

const onFinishFailed = (errorInfo) => {
  console.log('Failed:', errorInfo)
}
</script>

<template>
  <a-card id="task-card" size="small">
    <a-form
      layout="vertical"
      name="taskForm"
      :model="task_form"
      @finish="onFinish"
      @finishFailed="onFinishFailed"
    >
      <a-form-item
        label="Task name"
        name="name"
        :rules="[{ required: true, message: 'Please enter task name!' }]"
      >
        <a-input v-model:value="task_form.name"></a-input>
      </a-form-item>

      <a-form-item>
        <a-button type="primary" html-type="submit">Add</a-button>
      </a-form-item>
    </a-form>
  </a-card>
</template>

<style scoped>
#task-card {
  width: 320px;
  margin-top: 10px;
}
</style>