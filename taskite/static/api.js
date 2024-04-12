import Cookies from 'js-cookie'
import axios from 'axios'

const csrftoken = Cookies.get('csrftoken')

export const http = axios.create({
  baseURL: '/api',
  headers: {
    'X-CSRFToken': csrftoken,
  },
})

export const loginAPI = (data) => http.post('/home/login/', data)

export const projectListAPI = () => http.get('/projects/')
export const projectMemberListAPI = (id) => http.get(`/projects/${id}/members/`)

export const stateListAPI = (project_id) => http.get(`/projects/${project_id}/states/`)
export const stateTaskListAPI = (project_id, id) => http.get(`/projects/${project_id}/states/${id}/tasks/`)