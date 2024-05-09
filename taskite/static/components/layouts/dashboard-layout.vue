<template>
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
          <ProjectOutlined />
          <span>Projects</span>
        </a-menu-item>
        <a-menu-item key="notifications">
          <NotificationOutlined />
          <span>Notifications</span>
        </a-menu-item>
        <a-sub-menu key="settings">
          <template #title>
            <span>
              <SettingOutlined />
              <span>Settings</span>
            </span>
          </template>
          <a-menu-item key="settings-members"
            ><a href="/settings/users/">Users</a></a-menu-item
          >
          <a-menu-item key="settings-profile"><a href="/settings/profile/">Profile</a></a-menu-item>
          <a-menu-item key="settings-preferences">Preferences</a-menu-item>
        </a-sub-menu>
        <a-menu-item key="logout">
          <a href="/logout">
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
</template>
<script setup>
import {
  PieChartOutlined,
  DesktopOutlined,
  UserOutlined,
  TeamOutlined,
  FileOutlined,
  SettingOutlined,
  HomeOutlined,
  ProjectOutlined,
  NotificationOutlined
} from '@ant-design/icons-vue'
import { ref } from 'vue'

const props = defineProps(['page'])

const collapsed = ref(false)
const selectedKeys = ref([props.page])
</script>
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
