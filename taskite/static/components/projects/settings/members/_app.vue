<script setup>
import ProjectSettingsLayout from '@/components/layouts/project-settings-layout.vue'
const props = defineProps(['projectSlug'])

</script>

<template>
    <ProjectSettingsLayout page="members" :projectSlug="props.projectSlug">
        <h1>Members</h1>
    </ProjectSettingsLayout>
</template>