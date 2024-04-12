import { createApp } from 'vue'
import Antd from 'ant-design-vue'
import ProjectCreate from '@/components/projects/create.vue'
import 'ant-design-vue/dist/reset.css'
const props = JSON.parse(document.getElementById('props').textContent)

const app = createApp(ProjectCreate, { ...props })

app.use(Antd).mount('#app')
