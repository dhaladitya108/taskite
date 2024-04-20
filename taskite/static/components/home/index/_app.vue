<script setup>
import { ref, onMounted } from 'vue'
import { projectListAPI } from '@/utils/api'
import dashboard from '@/components/layouts/dashboard.vue'
import Project from '@/components/home/index/project.vue'

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
</script>

<template>
  <dashboard selectedPage="home">
    <div style="margin-bottom: 20px">
      <a-flex justify="space-between">
        <a-input-search
          v-model:value="projectSearchValue"
          placeholder="Search projects"
          style="width: 300px"
          @search="searchProject"
        />
        <a-button type="primary">Add project +</a-button>
      </a-flex>
    </div>

    <div>
      <a-row :gutter="16">
        <a-col
          v-for="project in projects"
          :key="project.id"
          class="gutter-row"
          :span="6"
        >
          <Project :project="project" />
        </a-col>
      </a-row>
    </div>
  </dashboard>
</template>
