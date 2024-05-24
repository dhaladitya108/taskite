<script setup>
import { ref, onMounted } from 'vue'
import { projectListAPI } from '@/api/projects'
import DashboardLayout from '@/components/layouts/dashboard-layout.vue'
import ProjectCard from '@/components/projects/list/project-card.vue'
import ProjectAddModal from '@/components/projects/list/project-add-modal.vue'

const projects = ref([])
const projectSearchValue = ref('')

onMounted(async () => {
  try {
    const { data } = await projectListAPI()
    projects.value = data
  } catch (error) {
    message.error('Failed to fetch projects')
  }
})

const searchProject = (searchValue) => {
  console.log('use value', searchValue)
  console.log('or use this.value', searchValue.value)
}

const showAddProjectModal = ref(false)
</script>

<template>
  <dashboard-layout page="projects">
    <div class="tk-main-content">
      <div style="margin-bottom: 20px">
        <a-flex justify="space-between">
          <a-input-search
            v-model:value="projectSearchValue"
            placeholder="Search projects"
            style="width: 300px"
            @search="searchProject"
          />
          <a-button type="primary" @click="() => (showAddProjectModal = true)"
            >Add project +</a-button
          >
        </a-flex>
      </div>

      <div>
        <a-row :gutter="16">
          <a-col
            v-for="project in projects"
            :key="project.id"
            class="gutter-row"
            :span="8"
          >
            <project-card :project="project"></project-card>
          </a-col>
        </a-row>
      </div>

      <a-modal
        :footer="false"
        title="Add project"
        v-model:open="showAddProjectModal"
      >
        <project-add-modal></project-add-modal>
      </a-modal>
    </div>
  </dashboard-layout>
</template>
