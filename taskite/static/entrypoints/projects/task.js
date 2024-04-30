import { createApp } from 'vue'
import Antd from 'ant-design-vue'
import ProjectTask from '@/components/projects/task/_app.vue'
import 'ant-design-vue/dist/reset.css'
const props = JSON.parse(document.getElementById('props').textContent)

const app = createApp(ProjectTask, { ...props })

app.use(Antd).mount('#app')
