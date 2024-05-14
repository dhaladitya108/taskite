<script setup>
import { computed, ref } from 'vue'
import { message } from 'ant-design-vue'
import ProjectSettingsLayout from '@/components/layouts/project-settings-layout.vue'
import {
  ProjectOutlined,
  AlignLeftOutlined,
  SaveOutlined,
} from '@ant-design/icons-vue'
import { storagePresignedURL, projectUpdateAPI } from '@/utils/api'
import { generateAvatar } from '@/utils/generators'
import { getBase64 } from '@/utils/helpers'

const props = defineProps(['project', 'role'])

const projectForm = ref({
  ...props.project,
})
const loading = ref(false)
const imageLoading = ref(false)
const uploadDataParams = ref({})
const uploadUrl = ref('')

const coverImageUrl = computed(() => {
  if (!!projectForm.value.coverUrl) {
    return projectForm.value.coverUrl
  }

  return generateAvatar(projectForm.value.name)
})

const handleChange = (info) => {
  if (info.file.status === 'uploading') {
    imageLoading.value = true
    return
  }
  if (info.file.status === 'done') {
    // Get this url from response in real world.
    getBase64(info.file.originFileObj, (base64Url) => {
      projectForm.value.coverUrl = base64Url
      imageLoading.value = false
    })
  }
  if (info.file.status === 'error') {
    imageLoading.value = false
    message.error('upload error')
  }
}

const handleCoverImageUpload = (file) => {
  return new Promise(async (resolve) => {
    try {
      const storageParams = {
        filename: file.name,
      }

      const { data } = await storagePresignedURL(storageParams)

      uploadUrl.value = data.url
      uploadDataParams.value = data.fields

      resolve()

      projectForm.value.cover = data.resourceName
    } catch (error) {
      console.log(error)
    } finally {
    }
  })
}

const updateProject = async (projectData) => {
  try {
    loading.value = true
    const { data } = await projectUpdateAPI(props.project.id, projectData)
    message.success(data.detail)
    projectForm.value = data.project
  } catch (error) {
    console.log(error)
  } finally {
    loading.value = false
  }
}

const onFinish = (values) => {
  console.log(values)
  updateProject(values)
}

const generateProjectSlug = (event) => {
  const projectName = event.target.value
  projectForm.value.slug = projectName
    .toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
}

const resetThemeColor = () => {
  projectForm.value.themeColor = "#1677ff"
}
</script>

<template>
  <ProjectSettingsLayout page="general" :projectSlug="projectForm.slug" :themeColor="props.project.themeColor">
    <div class="tk-breadcrump">
      <a-breadcrumb>
        <a-breadcrumb-item>
          <project-outlined></project-outlined>
          <span>Projects</span>
        </a-breadcrumb-item>
        <a-breadcrumb-item
          ><a :href="`/${projectForm.slug}/`">{{
            projectForm.name
          }}</a></a-breadcrumb-item
        >
        <a-breadcrumb-item>
          <a :href="`/${projectForm.slug}/settings/general/`">
            <align-left-outlined></align-left-outlined>
            <span style="margin-left: 4px">General</span>
          </a>
        </a-breadcrumb-item>
      </a-breadcrumb>
    </div>
    <a-flex justify="center" id="general-form">
      <a-form
        layout="vertical"
        :model="projectForm"
        id="general"
        @finish="onFinish"
        :disabled="props.role !== 'admin'"
      >
        <a-form-item name="cover">
          <a-upload
            name="file"
            :action="uploadUrl"
            :data="uploadDataParams"
            :before-upload="handleCoverImageUpload"
            :multiple="false"
            :show-upload-list="false"
            @change="handleChange"
          >
            <div class="cover-image">
              <img :src="coverImageUrl" alt="Cover Image" />
            </div>
          </a-upload>
        </a-form-item>
        <a-row :gutter="16">
          <a-col :span="12">
            <a-form-item label="Project Name" name="name">
              <a-input
                v-model:value="projectForm.name"
                @change="generateProjectSlug"
              />
            </a-form-item>

            <a-form-item label="Project ID" name="projectId">
              <a-input v-model:value="projectForm.projectId" />
            </a-form-item>

            <a-form-item label="Theme color" name="themeColor">
              <a-flex align="center" gap="middle">
                <a-input type="color" v-model:value="projectForm.themeColor" class="w-12"></a-input>
                <a @click="resetThemeColor">Reset</a>
              </a-flex>
            </a-form-item>
          </a-col>

          <a-col :span="12">
            <a-form-item label="Project Slug" name="slug">
              <a-input v-model:value="projectForm.slug" />
            </a-form-item>

            <a-form-item label="Project Visibility" name="visibility">
              <a-select ref="select" v-model:value="projectForm.visibility">
                <a-select-option value="private">Private</a-select-option>
                <a-select-option value="public">Public</a-select-option>
              </a-select>
            </a-form-item>
          </a-col>
        </a-row>

        <a-form-item label="Description" name="description">
          <a-textarea
            v-model:value="projectForm.description"
            :rows="5"
          ></a-textarea>
        </a-form-item>

        <a-form-item>
          <a-button :loading="loading" type="primary" html-type="submit">
            <template #icon>
              <save-outlined></save-outlined>
            </template>
            Save changes
          </a-button>
        </a-form-item>
      </a-form>
    </a-flex>
  </ProjectSettingsLayout>
</template>

<style scoped>
#general-form {
  margin-top: 50px;
}

.cover-image {
  position: relative;
  width: 600px;
  height: 150px; /* Adjust height as needed */
  overflow: hidden;
  border-radius: 5px;
}

.cover-image img {
  width: 100%;
  height: auto;
  object-fit: cover; /* Make sure the image covers the container */
}
</style>
