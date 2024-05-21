<script setup>
import { ref, onMounted, computed } from 'vue'
import { message } from 'ant-design-vue';
import { LoadingOutlined } from '@ant-design/icons-vue'

import { storagePresignedURL, profileUpdateAPI } from '@/utils/api'
import { generateAvatar } from '@/utils/generators'
import { getBase64 } from '@/utils/helpers'

import DashboardLayout from '@/components/layouts/dashboard-layout.vue'

const props = defineProps(['profile'])

const profileForm = ref({
  ...props.profile,
})
const imageLoading = ref(false)
const loading = ref(false)
const uploadDataParams = ref({})
const uploadUrl = ref('')

const handleChange = info => {
  if (info.file.status === 'uploading') {
    imageLoading.value = true;
    return;
  }
  if (info.file.status === 'done') {
    // Get this url from response in real world.
    getBase64(info.file.originFileObj, base64Url => {
      profileForm.value.avatarUrl = base64Url;
      imageLoading.value = false;
    });
  }
  if (info.file.status === 'error') {
    imageLoading.value = false;
    message.error('upload error');
  }
};

const handleAvatarUpload = (file) => {
  return new Promise(async (resolve) => {
    try {
      const storageParams = {
        filename: file.name,
      }

      const { data } = await storagePresignedURL(storageParams)

      uploadUrl.value = data.url
      uploadDataParams.value = data.fields

      resolve()

      // profileForm.value.avatarUrl = URL.createObjectURL(file)
      profileForm.value.avatar = data.resourceName
    } catch (error) {
      console.log(error)
    } finally {
    }
  })
}

const updateProfile = async (values) => {
  try {
    loading.value = true
    const { data } = await profileUpdateAPI(values)
    profileForm.value = data.profile
    message.success(data.detail)
  } catch (error) {
    console.log(error)
  } finally {
    loading.value = false
  }
}

const avatarImageUrl = computed(() => {
  if (!!profileForm.value.avatarUrl) {
    return profileForm.value.avatarUrl
  }

  return generateAvatar(profileForm.value.fullName)
})
</script>

<template>
  <dashboard-layout>
    <div id="profile-form">
      <a-flex justify="center">
        <a-form :model="profileForm" layout="vertical" @finish="updateProfile">
          <a-form-item name="avatar" v-model="profileForm.avatar">
            <a-upload :multiple="false" :show-upload-list="false" name="file" :action="uploadUrl"
              :data="uploadDataParams" :before-upload="handleAvatarUpload" @change="handleChange">
              <a-avatar v-if="imageLoading" shape="square" :size="72">
                <template #icon>
                  <LoadingOutlined />
                </template>
              </a-avatar>
              <a-avatar v-else :src="avatarImageUrl" shape="square" :size="72">
              </a-avatar>
            </a-upload>
          </a-form-item>

          <a-form-item>
            <a-flex vertical>
              <div id="title">{{ profileForm.fullName }}</div>
              <div>{{ profileForm.email }}</div>
            </a-flex>
          </a-form-item>
          <a-row :gutter="16">
            <a-col :span="12">
              <a-form-item label="Full name" name="fullName">
                <a-input v-model:value="profileForm.fullName" />
              </a-form-item>

              <a-form-item label="Display name" name="displayName">
                <a-input v-model:value="profileForm.displayName" />
              </a-form-item>
            </a-col>

            <a-col :span="12">
              <a-form-item label="Username" name="username">
                <a-input v-model:value="profileForm.username" />
              </a-form-item>

              <a-form-item label="Email">
                <a-input v-model:value="profileForm.email" :disabled="true" />
              </a-form-item>
            </a-col>
          </a-row>

          <a-form-item>
            <a-button :loading="loading" type="primary" html-type="submit">Save changes</a-button>
          </a-form-item>
        </a-form>
      </a-flex>
    </div>
  </dashboard-layout>
</template>

<style scoped>
#profile-form {
  margin-top: 50px;
}

#title {
  font-size: x-large;
  font-weight: bold;
}
</style>
