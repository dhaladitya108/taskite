import { http } from '@/api/http'

export const projectCreateAPI = (data) => http.post('/projects/', data)

export const projectListAPI = () => http.get('/projects/')

export const projectUpdateAPI = (projectId, data) =>
  http.patch(`/projects/${projectId}/`, data)

export const projectInvitesAPI = () => http.get('/projects/invites/')

export const projectMembersAPI = (projectId) =>
  http.get(`/projects/${projectId}/members/`)
