<template>
  <a-layout>
    <a-layout-sider v-model:collapsed="collapsed" :trigger="null" collapsible>
      <div class="logo" />
      <a-menu v-model:selectedKeys="selectedPage" theme="dark" mode="inline">
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
        <a-menu-item key="members">
          <UserOutlined />
          <span>Members</span>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout style="height: 100vh">
      <a-layout-header style="background: #fff; padding: 0">
        <MenuUnfoldOutlined
          v-if="collapsed"
          class="trigger"
          @click="() => (collapsed = !collapsed)"
        />
        <MenuFoldOutlined
          v-else
          class="trigger"
          @click="() => (collapsed = !collapsed)"
        />
      </a-layout-header>
      <a-layout-content
        :style="{
          margin: '24px 16px',
          padding: '24px',
          background: '#fff',
          overflowX: 'auto'
        }"
      >
        <slot></slot>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>
<script setup>
import { ref } from "vue";
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined,
  VideoCameraOutlined,
  UploadOutlined,
  HomeOutlined,
  ProjectOutlined
} from "@ant-design/icons-vue";
const props = defineProps(["selectedPage"]);

const selectedPage = ref([props.selectedPage]);

const collapsed = ref(false);
</script>
<style>
.trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

.trigger:hover {
  color: #1890ff;
}

.logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.3);
  margin: 16px;
}

.site-layout .site-layout-background {
  background: #fff;
}
</style>
