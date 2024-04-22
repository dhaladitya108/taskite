<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { stateListAPI, projectMemberListAPI, taskUpdateAPI } from '@/utils/api'
import { VueDraggable } from 'vue-draggable-plus'

import dashboard from '@/components/layouts/dashboard.vue'
import Task from '@/components/projects/detail/task.vue'
import Filters from '@/components/projects/detail/filters.vue'

const props = defineProps(['project'])
const project = ref(props.project)
const members = ref([])
const states = ref([])

const selectedPriorities = ref([])
const selectedAssignees = ref([])

const fetchStates = async (params={}) => {
  try {
    const { data } = await stateListAPI(project.value.id, params)
    states.value = data
  } catch (error) {
    console.log(error)
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

onMounted(() => {
  fetchMembers()
  fetchStates()
})

watch([selectedPriorities, selectedAssignees], async () => {
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
  const params = {}
  if (newFilters.selectedPriorities.length > 0) {
    params['priorities'] = newFilters.selectedPriorities
  }

  if (newFilters.selectedAssignees.length > 0) {
    params['assignees'] = newFilters.selectedAssignees
  }
  fetchStates(params)
}
</script>

<template>
  <dashboard selectedPage="projects">
    <a-flex justify="space-between" style="padding: 10px">
      <div></div>
      <div>
        <Filters :members="members" @filterChange="reloadTasksWithNewFilters" />
      </div>
    </a-flex>

    <a-flex gap="middle" align="start">
      <div v-for="state in states" :key="state.id">
        <div>
          <a-typography-title :level="5">{{ state.name }}</a-typography-title>
          <VueDraggable
            v-model="state.tasks"
            id="tk-drag"
            group="tasks"
            @update="(event) => onUpdate(event, state.id)"
            @add="(event) => onAdd(event, state.id)"
          >
            <Task v-for="task in state.tasks" :key="task.id" :task="task" />
          </VueDraggable>
        </div>
      </div>
    </a-flex>
  </dashboard>
</template>

<style scoped>
#tk-drag {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>
