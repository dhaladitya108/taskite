import { http } from '@/api/http'

export const projectInviteListAPI = (projectId) =>
  http.get(`/projects/${projectId}/project_invites/`)

export const projectInviteDeleteAPI = (projectId, projectInviteId) =>
  http.delete(`/projects/${projectId}/project_invites/${projectInviteId}/`)
