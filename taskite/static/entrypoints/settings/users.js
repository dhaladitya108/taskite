import { createApp } from 'vue'
import Antd from 'ant-design-vue'
import UsersApp from '@/components/settings/users/_app.vue'
import 'ant-design-vue/dist/reset.css'
import '@/css/app.css'

const props = JSON.parse(document.getElementById('props').textContent)

const app = createApp(UsersApp, { ...props })

app.use(Antd).mount('#app')
