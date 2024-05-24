import { http } from '@/api/http'

export const projectMembersListAPI = (projectId) =>
  http.get(`/projects/${projectId}/project_members/`)

export const projectMemberUpdateAPI = (
  projectId,
  projectMemberId,
  updatedData
) =>
  http.patch(
    `/projects/${projectId}/project_members/${projectMemberId}/`,
    updatedData
  )

export const projectMemberInviteAPI = (projectId, data) =>
  http.post(`/projects/${projectId}/project_members/invite/`, data)
