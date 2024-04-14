<template>
  <a-layout style="min-height: 100vh">
    <a-layout-sider v-model:collapsed="collapsed" collapsible>
      <div class="logo" />
      <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
        <a-menu-item key="home">
          <pie-chart-outlined />
          <span>Home</span>
        </a-menu-item>
        <a-menu-item key="projects">
          <desktop-outlined />
          <span>Projects</span>
        </a-menu-item>
        <a-sub-menu key="settings">
          <template #title>
            <span>
              <user-outlined />
              <span>Settings</span>
            </span>
          </template>
          <a-menu-item key="settings-members">Members</a-menu-item>
          <a-menu-item key="settings-profile">Profile</a-menu-item>
          <a-menu-item key="settings-preferences">Preferences</a-menu-item>
        </a-sub-menu>
        <a-menu-item key="logout">
          <file-outlined />
          <span>Logout</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-content style="margin: 16px 16px; overflow-x: auto;">
        <slot></slot>
      </a-layout-content>
      <a-layout-footer style="text-align: center">
        Ant Design ©2018 Created by Ant UED
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>
<script lang="ts" setup>
import {
  PieChartOutlined,
  DesktopOutlined,
  UserOutlined,
  TeamOutlined,
  FileOutlined,
} from "@ant-design/icons-vue";
import { ref } from "vue";
const collapsed = ref<boolean>(false);
const selectedKeys = ref<string[]>(["1"]);
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
[data-theme="dark"] .site-layout .site-layout-background {
  background: #141414;
}
</style>
