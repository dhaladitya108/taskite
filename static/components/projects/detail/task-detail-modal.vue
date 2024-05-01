<script setup>
import { ref, onMounted, computed } from 'vue'
import { taskDetailAPI, taskUpdateAPI } from '@/utils/api'
import { generateAvatar } from '@/utils/generators'

import LoadingSpinner from '@/components/common/loading-spinner.vue'
import BaseEditor from '@/components/common/base-editor.vue'

const props = defineProps([
  'taskId',
  'projectId',
  'projectSlug',
  'projectName',
  'members',
])
const emit = defineEmits(['updated'])

const bordered = ref(false)

const task = ref(null)
const fetchTaskDetail = async () => {
  try {
    const { data } = await taskDetailAPI(props.projectId, props.taskId)
    task.value = data
    name.value = data.name
    description.value = data.description
    assigneeIds.value = data.assignees.map((assignee) => assignee.id)
  } catch (error) {
    console.log(error)
  }
}
const updateTask = async (payload) => {
  try {
    await taskUpdateAPI(props.projectId, task.value.id, payload, {})
  } catch (error) {
    console.log(error)
  }
}

onMounted(async () => {
  fetchTaskDetail()
})

const name = ref('')
const handleNameUpdate = async () => {
  bordered.value = false

  if (name.value !== task.value.name) {
    updateTask({ name: name.value })
    task.value.name = name.value

    emit('updated', { name: name.value })
  }
}

const description = ref('')
const handleDescriptionUpdate = async () => {
  if (description.value !== task.value.description) {
    updateTask({ description: description.value })
    task.value.description = description.value
  }
}

const handlePriorityChange = (value) => {
  updateTask({ priority: value })
  emit('updated', { priority: value })
}

const handleTaskTypeChange = (value) => {
  updateTask({ taskType: value })
  emit('updated', { taskType: value })
}

const assigneeIds = ref([])
const handleAssigneeChange = (values) => {
  updateTask({ assigneeIds: values })
  emit('updated', { assignees: props.members.filter((member) => values.includes(member.id)) })
}
</script>

<template>
  <div v-if="!!task">
    <a-breadcrumb>
      <a-breadcrumb-item>
        <a :href="`/${props.projectSlug}/`">{{ props.projectName }}</a>
      </a-breadcrumb-item>
      <a-breadcrumb-item>
        <a :href="`/${props.projectSlug}/${task.taskId}/`">{{ task.taskId }}</a>
      </a-breadcrumb-item>
    </a-breadcrumb>

    <a-input
      size="large"
      v-model:value="name"
      :bordered="bordered"
      @focus="() => (bordered = true)"
      @blur="handleNameUpdate"
    ></a-input>
    <a-row :gutter="16">
      <a-col :span="16">
        <div>Description</div>
        <base-editor
          v-model="description"
          @blur="handleDescriptionUpdate"
        ></base-editor>
      </a-col>
      <a-col :span="8">
        <a-flex>
          <a-form
            layout="horizontal"
            :wrapper-col="{
              span: 14,
            }"
            :label-col="{
              style: {
                width: '120px',
              },
            }"
          >
            <a-form-item label="Priority">
              <a-select
                ref="select"
                v-model:value="task.priority"
                @change="handlePriorityChange"
              >
                <a-select-option value="low">Low</a-select-option>
                <a-select-option value="medium">Medium</a-select-option>
                <a-select-option value="high">High</a-select-option>
                <a-select-option value="urgent">Urgent</a-select-option>
              </a-select>
            </a-form-item>

            <a-form-item label="Task type">
              <a-select
                ref="select"
                v-model:value="task.taskType"
                @change="handleTaskTypeChange"
              >
                <a-select-option value="issue">Issue</a-select-option>
                <a-select-option value="task">Task</a-select-option>
                <a-select-option value="story">Story</a-select-option>
                <a-select-option value="bug">Bug</a-select-option>
                <a-select-option value="epic">Epic</a-select-option>
              </a-select>
            </a-form-item>

            <a-form-item label="Assignee">
              <a-select
                v-model:value="assigneeIds"
                mode="multiple"
                option-label-prop="children"
                @change="handleAssigneeChange"
              >
                <a-select-option
                  :value="member.id"
                  :label="member.displayName"
                  v-for="member in props.members"
                >
                  <span role="img"
                    ><a-avatar
                      size="small"
                      :src="generateAvatar(member.fullName)"
                    >
                    </a-avatar>
                    {{ member.displayName }}
                  </span>
                </a-select-option>
              </a-select>
            </a-form-item>
          </a-form>
        </a-flex>
      </a-col>
    </a-row>
  </div>
  <div v-else>
    <a-flex justify="center" align="center" style="height: 40vh">
      <loading-spinner />
    </a-flex>
  </div>
</template>
