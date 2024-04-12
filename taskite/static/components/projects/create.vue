<script setup>
import Dashboard from "@/components/Dashboard.vue";

import { ref, onMounted, computed } from "vue";
import { stateListAPI, projectMemberListAPI, stateTaskListAPI } from "@/api";

const newProjectForm = ref({
    name: '',
    description: '',
    visibility: 'private',
})

onMounted(async () => {
});
</script>

<template>
  <Dashboard selectedPage="projects">
    <a-flex :justify="center" :align="center" style="height: 100vh;">
        
    </a-flex>
  </Dashboard>
</template>

<style scoped>
</style>
