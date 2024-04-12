<script setup>
import Dashboard from "@/components/Dashboard.vue";
import Task from '@/components/projects/_task.vue'

import { ref, onMounted, computed } from "vue";
import { stateListAPI, projectMemberListAPI, stateTaskListAPI } from "@/api";
import { VueDraggable } from "vue-draggable-plus";

const props = defineProps(["project"]);

const project = ref(props.project);
const members = ref([]);
const states = ref([]);

const fetchStates = async () => {
  try {
    const { data } = await stateListAPI(project.value.id);
    states.value = data;

    console.log("----> States :: ", states);
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

// const fetchStateTasks = async (project_id, state_id) => {
//   try {
//     const { data } = await stateTaskListAPI(project_id, state_id);
//     return data;
//   } catch (error) {
//     console.log(error);
//     return [];
//   }
// };

onMounted(async () => {
  fetchMembers();
  fetchStates();
});
</script>

<template>
  <Dashboard selectedPage="projects">
    <a-flex gap="middle" align="start">
      <div v-for="state in states" :key="state.id">
        <div>
          <a-typography-title :level="5">{{ state.name }}</a-typography-title>
          <VueDraggable v-model="state.tasks" id="tk-drag" group="tasks">
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
