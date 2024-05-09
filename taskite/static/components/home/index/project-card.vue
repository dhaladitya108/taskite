<script setup>
const { project } = defineProps(['project'])
</script>

<template>
  <a :href="`/${project.slug}/`">
    <a-card class="project-card">
      <a-typography-title :level="5">{{ project.name }}</a-typography-title>
      <div>{{ project.description }}</div>
    </a-card>
  </a>
</template>

<style scoped>
.project-card {
  height: 120px;
}
</style>
