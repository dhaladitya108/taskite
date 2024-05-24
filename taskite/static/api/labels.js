import { http } from '@/api/http'

export const labelListAPI = (project_id) =>
  http.get(`/projects/${project_id}/labels/`)
