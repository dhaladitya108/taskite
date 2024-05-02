<script setup>
import ProjectSettingsLayout from '@/components/layouts/project-settings-layout.vue'
const props = defineProps(['projectSlug'])

</script>

<template>
    <ProjectSettingsLayout page="general" :projectSlug="props.projectSlug">
        <h1>General</h1>
    </ProjectSettingsLayout>
</template>