import { http } from '@/api/http'

export const stateTaskListAPI = (projectId, params) =>
  http.get(`/projects/${projectId}/states/`, {
    params: {
      ...params,
      include: 'tasks',
    },
  })
