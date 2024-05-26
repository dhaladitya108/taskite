<script setup>
import { reactive } from 'vue'
import { projectCreateAPI } from '@/api/projects'

const projectAddForm = reactive({
  name: '',
  description: '',
  visibility: 'private',
})

const createNewProject = async (values) => {
  try {
    const { data } = await projectCreateAPI(values)
    window.location.href = `/${data.project.slug}/`
  } catch (error) {
    console.log(error)
  }
}
</script>

<template>
  <a-form layout="vertical" :model="projectAddForm" @finish="createNewProject">
    <a-form-item
      label="Name"
      name="name"
      :rules="[{ required: true, message: 'Please enter project name!' }]"
    >
      <a-input v-model:value="projectAddForm.name" />
    </a-form-item>
    <a-form-item label="Description" name="description">
      <a-textarea v-model:value="projectAddForm.description" :rows="5" />
    </a-form-item>
    <a-form-item>
      <a-button type="primary" html-type="submit">Add</a-button>
    </a-form-item>
  </a-form>
</template>
