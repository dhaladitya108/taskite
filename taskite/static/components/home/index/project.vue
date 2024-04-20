<script setup>
const { project } = defineProps(['project'])
</script>

<template>
  <a :href="`/${project.slug}/`">
    <a-card>
      <p>{{ project.name }}</p>
    </a-card>
  </a>
</template>
