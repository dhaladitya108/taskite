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

export const stateTaskListAPI = (project_id, params) =>
  http.get(`/projects/${project_id}/states/`, {
    params: {
      ...params,
      include: 'tasks',
    },
  })

export const taskUpdateAPI = (project_id, task_id, data, params) =>
  http.patch(`/projects/${project_id}/tasks/${task_id}/`, data, {
    params,
  })

export const task_add_api = (project_id, data, params = {}) =>
  http.post(`/projects/${project_id}/tasks/`, data, {
    params,
  })

export const labelListAPI = (project_id) =>
  http.get(`/projects/${project_id}/labels/`)
