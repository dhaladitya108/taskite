<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import {
  stateTaskListAPI,
  projectMemberListAPI,
  taskUpdateAPI,
  labelListAPI,
} from '@/utils/api'
import { VueDraggable } from 'vue-draggable-plus'
// import { OnClickOutside } from '@vueuse/components'

import DashboardLayout from '@/components/dashboard-layout.vue'
import TaskCard from '@/components/projects/detail/task-card.vue'
import TaskFilters from '@/components/projects/detail/task-filters.vue'
import LoadingSpinner from '@/components/common/loading-spinner.vue'
import TaskAddForm from '@/components/projects/detail/task-add-form.vue'

const props = defineProps(['project'])

const loading = ref(false)
const project = ref(props.project)
const members = ref([])
const states = ref([])
const labels = ref([])
const selectedPriorities = ref([])
const selectedAssignees = ref([])
const selectedLabels = ref([])
const task_add_active_form = ref('')

const fetchStates = async (params = {}) => {
  try {
    loading.value = true
    const { data } = await stateTaskListAPI(project.value.id, params)
    states.value = data
  } catch (error) {
    console.log(error)
  } finally {
    loading.value = false
  }
}

const fetchMembers = async () => {
  try {
    const { data } = await projectMemberListAPI(project.value.id)
    members.value = data
  } catch (error) {
    console.log(error)
  }
}

const fetchLabels = async () => {
  try {
    const { data } = await labelListAPI(project.value.id)
    labels.value = data
  } catch (error) {
    console.log(error)
  }
}

onMounted(() => {
  fetchMembers()
  fetchLabels()
  fetchStates()
})

watch([selectedPriorities, selectedAssignees, selectedLabels], async () => {
  fetchStates()
})

async function onUpdate(event, state_id) {
  const selected_state = states.value.find((s) => s.id === state_id)
  const current_task = selected_state.tasks[event.newIndex]
  const updated_data = {}

  if (event.newIndex === 0) {
    let next_task = selected_state.tasks[event.newIndex + 1]
    updated_data['order'] = next_task.order / 2
  } else if (event.newIndex === selected_state.tasks.length - 1) {
    let previous_task = selected_state.tasks[event.newIndex - 1]
    updated_data['order'] = previous_task.order / 2
  } else {
    let next_task = selected_state.tasks[event.newIndex + 1]
    let previous_task = selected_state.tasks[event.newIndex - 1]
    updated_data['order'] = (next_task.order + previous_task.order) / 2
  }

  try {
    const { data } = await taskUpdateAPI(
      project.value.id,
      current_task.id,
      updated_data
    )
    current_task.order = data.task.order
  } catch (error) {
    console.log(error)
  }
}
async function onAdd(event, state_id) {
  const selected_state = states.value.find((s) => s.id === state_id)
  const current_task = selected_state.tasks[event.newIndex]
  const updated_data = { state_id: selected_state.id }

  if (event.newIndex === 0) {
    let next_task = selected_state.tasks[event.newIndex + 1]
    updated_data['order'] = next_task.order / 2
  } else if (event.newIndex === selected_state.tasks.length - 1) {
    let previous_task = selected_state.tasks[event.newIndex - 1]
    updated_data['order'] = previous_task.order + 10000
  } else {
    let next_task = selected_state.tasks[event.newIndex + 1]
    let previous_task = selected_state.tasks[event.newIndex - 1]
    updated_data['order'] = (next_task.order + previous_task.order) / 2
  }

  try {
    const { data } = await taskUpdateAPI(
      project.value.id,
      current_task.id,
      updated_data
    )
    current_task.order = data.task.order
  } catch (error) {
    console.log(error)
  }
}

function reloadTasksWithNewFilters(newFilters) {
  console.log(newFilters)

  const params = {}
  if (newFilters.selectedPriorities.length > 0) {
    params['priorities'] = newFilters.selectedPriorities
  }

  if (newFilters.selectedAssignees.length > 0) {
    params['assignees'] = newFilters.selectedAssignees
  }

  if (newFilters.selectedLabels.length > 0) {
    params['labels'] = newFilters.selectedLabels
  }

  fetchStates(params)
}

function addNewTask(state_id, new_task) {
  const selected_state = states.value.find((s) => s.id === state_id)
  selected_state.tasks.push({
    ...new_task,
    assignees: [],
  })

  task_add_active_form.value = ''
}

function activate_task_add_form(state_id) {
  task_add_active_form.value = state_id
}
</script>

<template>
  <dashboard-layout selectedPage="projects">
    <a-flex justify="space-between" style="margin-bottom: 15px">
      <div>
        <a-typography-title :level="4">{{ project.name }}</a-typography-title>
      </div>
      <div>
        <task-filters
          :members="members"
          :labels="labels"
          @filterChange="reloadTasksWithNewFilters"
        />
        <a-button type="primary">+ Add Task</a-button>
      </div>
    </a-flex>

    <hr />

    <a-flex justify="center" align="center" style="height: 90vh" v-if="loading">
      <loading-spinner />
    </a-flex>
    <a-flex gap="middle" align="start" v-else>
      <div v-for="state in states" :key="state.id" style="min-width: 320px">
        <div>
          <a-typography-title :level="5">{{ state.name }}</a-typography-title>
          <VueDraggable
            v-model="state.tasks"
            id="tk-drag"
            group="tasks"
            @update="(event) => onUpdate(event, state.id)"
            @add="(event) => onAdd(event, state.id)"
          >
            <task-card
              v-for="task in state.tasks"
              :key="task.id"
              :task="task"
              :project="project"
            />
          </VueDraggable>

          <a-typography-link
            v-show="task_add_active_form !== state.id"
            @click="activate_task_add_form(state.id)"
            >+ Add Task</a-typography-link
          >
          <task-add-form
            v-show="task_add_active_form === state.id"
            :state_id="state.id"
            :project_id="project.id"
            @newTaskAdded="addNewTask"
          ></task-add-form>
        </div>
      </div>
    </a-flex>
  </dashboard-layout>
</template>

<style scoped>
#tk-drag {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.add-task-popover {
  margin: 5px;
  padding: 5px;
}
</style>
