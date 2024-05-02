import Cookies from 'js-cookie'
import axios from 'axios'
import applyCaseMiddleware from 'axios-case-converter'

const csrftoken = Cookies.get('csrftoken')

const caseMiddleWareOptions = {
  ignoreHeaders: true,
}

export const http = applyCaseMiddleware(
  axios.create({
    baseURL: '/api',
    headers: {
      'X-CSRFToken': csrftoken,
    },
  }),
  caseMiddleWareOptions
)

export const loginAPI = (data) => http.post('/home/login/', data)

export const userListAPI = () => http.get('/users/')

export const projectCreateAPI = (data) => http.post('/projects/', data)
export const projectListAPI = () => http.get('/projects/')
export const projectMemberListAPI = (projectId) =>
  http.get(`/projects/${projectId}/members/`)

export const stateTaskListAPI = (projectId, params) =>
  http.get(`/projects/${projectId}/states/`, {
    params: {
      ...params,
      include: 'tasks',
    },
  })

export const taskUpdateAPI = (project_id, task_id, data, params) =>
  http.patch(`/projects/${project_id}/tasks/${task_id}/`, data, {
    params,
  })

export const taskAddAPI = (project_id, data, params = {}) =>
  http.post(`/projects/${project_id}/tasks/`, data, {
    params,
  })

export const taskDetailAPI = (projectId, taskId, params = {}) =>
  http.get(`/projects/${projectId}/tasks/${taskId}/`, params)

export const labelListAPI = (project_id) =>
  http.get(`/projects/${project_id}/labels/`)
