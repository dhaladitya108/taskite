import { createApp } from 'vue'
import Antd from 'ant-design-vue'
import LoginApp from '@/components/home/login/_app.vue'
import 'ant-design-vue/dist/reset.css'
const props = JSON.parse(document.getElementById('props').textContent)

const app = createApp(LoginApp, { ...props })

app.use(Antd).mount('#app')
