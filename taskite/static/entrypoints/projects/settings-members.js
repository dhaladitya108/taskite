import { createApp } from 'vue'
import Antd from 'ant-design-vue'
import MemberApp from '@/components/projects/settings/members/_app.vue'
import 'ant-design-vue/dist/reset.css'
import '@/css/app.css'

const props = JSON.parse(document.getElementById('props').textContent)

const app = createApp(MemberApp, { ...props })

app.use(Antd).mount('#app')
