<script setup>
import { reactive, ref, computed, onMounted } from 'vue'
import BaseEditor from '@/components/common/base-editor.vue'
import { taskUpdateAPI, task_detail_api } from '@/utils/api'

const props = defineProps(['task', 'project'])
const bordered = ref(false)

const task_form = reactive({
  description: props.task.description,
})
const onFinish = async (values) => {
  try {
    await taskUpdateAPI(props.project.id, props.task.id, values, {})
    props.task.description = values.description
  } catch (error) {
    console.log(error)
  }
}

const name = ref(props.task.name)
const handleNameUpdate = async () => {
  bordered.value = false

  if (name.value !== props.task.name) {
    try {
      await taskUpdateAPI(
        props.project.id,
        props.task.id,
        { name: name.value },
        {}
      )
      props.task.name = name.value
    } catch (error) {
      console.log(error)
    }
  }
}
const show_save_button = computed(
  () => task_form.description !== props.task.description
)
const show_cancel_button = computed(
  () => task_form.description !== props.task.description
)
const set_default_description = () => {
  task_form.description = props.task.description
}

const fetch_task_details = async () => {
  try {
    await task_detail_api(props.project.id, props.task.id)
  } catch (error) {
    console.log('Error')
  }
}

onMounted(() => {
  console.log('Mounted ---> ', props.task.task_id)
  fetch_task_details()
})
</script>

<template>
  <a-input
    size="large"
    v-model:value="name"
    :bordered="bordered"
    placeholder="Title"
    @focus="() => (bordered = true)"
    @blur="handleNameUpdate"
    :addon-before="props.task.task_id"
  >
    <!-- <template #prefix>
      {{ props.task.task_id }}
    </template> -->
  </a-input>
  <a-form :model="task_form" @finish="onFinish" layout="vertical">
    <a-form-item name="description" label="Description">
      <base-editor v-model="task_form.description"></base-editor>
    </a-form-item>
    <a-form-item>
      <a-space wrap>
        <a-button v-show="show_save_button" type="primary" htmlType="submit"
          >Save</a-button
        >
        <a-button
          v-show="show_cancel_button"
          type="dashed"
          @click="set_default_description"
          >Cancel</a-button
        >
      </a-space>
    </a-form-item>
  </a-form>
</template>
