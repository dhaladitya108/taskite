import { createApp } from 'vue'
import Antd from 'ant-design-vue'
import MembersApp from '@/components/settings/members/_app.vue'
import 'ant-design-vue/dist/reset.css'
const props = JSON.parse(document.getElementById('props').textContent)

const app = createApp(MembersApp, { ...props })

app.use(Antd).mount('#app')
