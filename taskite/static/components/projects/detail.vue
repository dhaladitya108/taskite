<script setup>
import Dashboard from "@/components/Dashboard.vue";
import Task from "@/components/projects/_task.vue";

import { ref, onMounted, computed, watch } from "vue";
import {
  stateListAPI,
  projectMemberListAPI,
  stateTaskListAPI,
  taskUpdateAPI,
} from "@/api";
import { VueDraggable } from "vue-draggable-plus";

const props = defineProps(["project"]);

const project = ref(props.project);
const members = ref([]);
const states = ref([]);
const selectedPriorities = ref([]);
const selectedAssignees = ref([]);

const priorityOptions = [
  { label: "Urgent", value: "urgent" },
  { label: "High", value: "high" },
  { label: "Medium", value: "medium" },
  { label: "Low", value: "low" },
];

const assigneeOptions = computed(() => {
  return members.value.map((member) => {
    return {
      label: member.display_name,
      value: member.id,
    };
  });
});

const fetchStates = async () => {
  const params = {};
  if (selectedPriorities.value.length > 0) {
    params["priorities"] = selectedPriorities.value;
  }

  if (selectedAssignees.value.length > 0) {
    params["assignees"] = selectedAssignees.value;
  }

  try {
    const { data } = await stateListAPI(project.value.id, params);
    states.value = data;
  } catch (error) {
    console.log(error);
  }
};

const fetchMembers = async () => {
  try {
    const { data } = await projectMemberListAPI(project.value.id);
    members.value = data;
  } catch (error) {
    console.log(error);
  }
};

const updateTask = async (task_id, taskDetails) => {
  try {
    await taskUpdateAPI(project.value.id, task_id, taskDetails);
  } catch (error) {
    console.log(error);
  }
};

onMounted(() => {
  fetchMembers();
  fetchStates();
});

watch([selectedPriorities, selectedAssignees], async () => {
  fetchStates();
});

function onUpdate(event, stateID) {
  const selectedState = states.value.find((s) => s.id === stateID);
  switch (event.newIndex) {
    case 0:
      console.log("Dragged to first");
      var selectedTask = selectedState.tasks[0];

      updateTask(selectedTask.id, { order: parseFloat(selectedState.tasks[1].order) / 2 });
      break;

    case selectedState.tasks.length - 1:
      console.log('Draaaag to end --- ')
      var selectedTask = selectedState.tasks[selectedState.tasks.length - 1];

      updateTask(selectedTask.id, { order: parseFloat(selectedState.tasks[1].order) + parseFloat(10000) });
      break;

    default:
      console.log("Dragged --->");
      break;
  }
}
function onAdd(event, newStateID) {}
function remove() {
  console.log("remove");
}
</script>

<template>
  <Dashboard selectedPage="projects">
    <a-flex justify="space-between">
      <div></div>
      <div>
        <a-dropdown :trigger="['click']">
          <a-button type="primary" size="small"> Filters </a-button>
          <template #overlay>
            <a-card size="small" style="width: 200px">
              <div>Priorities</div>
              <a-flex vertical>
                <a-checkbox-group
                  v-model:value="selectedPriorities"
                  :options="priorityOptions"
                >
                </a-checkbox-group>
              </a-flex>

              <div>Assignees</div>
              <a-flex vertical>
                <a-checkbox-group
                  v-model:value="selectedAssignees"
                  :options="assigneeOptions"
                >
                </a-checkbox-group>
              </a-flex>
            </a-card>
          </template>
        </a-dropdown>
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
            @remove="remove"
          >
            <Task v-for="task in state.tasks" :key="task.id" :task="task" />
          </VueDraggable>
        </div>
      </div>
    </a-flex>
  </Dashboard>
</template>

<style scoped>
#tk-drag {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
</style>
