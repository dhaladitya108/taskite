<script setup>
import {
  UserOutlined,
  SettingOutlined,
  HomeOutlined,
  ProjectOutlined,
  ShareAltOutlined,
} from '@ant-design/icons-vue'
import { ref, computed } from 'vue'

const props = defineProps({
  page: String,
  themeColor: {
    type: String,
    default: '#1677ff',
    required: false,
  },
})

const collapsed = ref(false)
const selectedKeys = ref([props.page])

const theme = computed(() => {
  return {
    token: {
      colorPrimary: props.themeColor,
      borderRadius: 5,
    },
  }
})
</script>
<template>
  <a-config-provider :theme="theme">
    <a-layout style="min-height: 100vh">
      <a-layout-sider v-model:collapsed="collapsed" collapsible>
        <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
          <a-menu-item key="home">
            <a href="/">
              <HomeOutlined />
              <span>Home</span>
            </a>
          </a-menu-item>
          <a-menu-item key="projects">
            <a href="/projects/">
              <ProjectOutlined />
              <span>Projects</span>
            </a>
          </a-menu-item>
          <a-menu-item key="notifications" disabled>
            <ShareAltOutlined />
            <span>Integrations</span>
          </a-menu-item>
          <a-sub-menu key="settings">
            <template #title>
              <span>
                <SettingOutlined />
                <span>Settings</span>
              </span>
            </template>
            <a-menu-item key="settings-profile"><a href="/settings/profile/">Profile</a></a-menu-item>
            <a-menu-item key="settings-preferences" disabled>Preferences</a-menu-item>
          </a-sub-menu>
          <a-menu-item key="logout">
            <a href="/accounts/logout/">
              <user-outlined />
              <span>Logout</span>
            </a>
          </a-menu-item>
        </a-menu>
      </a-layout-sider>
      <a-layout>
        <a-layout-content style="overflow-x: auto">
          <slot></slot>
        </a-layout-content>
        <!-- <a-layout-footer style="text-align: center">
          Ant Design ©2018 Created by Ant UED
        </a-layout-footer> -->
      </a-layout>
    </a-layout>
  </a-config-provider>
</template>
<style scoped>
.logo {
  height: 32px;
  margin: 16px;
  background: rgba(255, 255, 255, 0.3);
}

.site-layout .site-layout-background {
  background: #fff;
}

[data-theme='dark'] .site-layout .site-layout-background {
  background: #141414;
}
</style>
