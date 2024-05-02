<script setup>
import DashboardLayout from '@/components/layouts/dashboard-layout.vue'
import { AlignLeftOutlined, UserSwitchOutlined, DatabaseOutlined, HighlightOutlined } from '@ant-design/icons-vue';
const props = defineProps(['page', 'projectSlug'])

import { ref } from 'vue'
const onCollapse = (collapsed, type) => {
  // console.log(collapsed, type)
}

const selectedKeys = ref([props.page])
</script>

<template>
  <dashboard-layout page="projects">
    <a-layout>
      <a-layout-sider
        breakpoint="lg"
        collapsed-width="0"
        @collapse="onCollapse"
      >
        <!-- <div class="logo" /> -->
        <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
          <a-menu-item key="general">
            <a :href="`/${props.projectSlug}/settings/general/`">
              <align-left-outlined /> 
              <span class="nav-text">General</span>
            </a>
          </a-menu-item>
          <a-menu-item key="2">
            <database-outlined />
            <span class="nav-text">States</span>
          </a-menu-item>
          <a-menu-item key="3">
            <highlight-outlined />
            <span class="nav-text">Labels</span>
          </a-menu-item>
          <a-menu-item key="members">
            <a :href="`/${props.projectSlug}/settings/members/`">
              <user-switch-outlined />
              <span class="nav-text">Members</span>
            </a>
          </a-menu-item>
        </a-menu>
      </a-layout-sider>
      <a-layout>
        <a-layout-content :style="{ margin: '24px 16px 0' }">
          <div
            :style="{ padding: '24px', background: '#fff', minHeight: '100vh' }"
          >
            <slot></slot>
          </div>
        </a-layout-content>
      </a-layout>
    </a-layout>
  </dashboard-layout>
</template>

<style scoped>
.logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}

.site-layout-sub-header-background {
  background: #fff;
}

.site-layout-background {
  background: #fff;
}

[data-theme='dark'] .site-layout-sub-header-background {
  background: #141414;
}
</style>
