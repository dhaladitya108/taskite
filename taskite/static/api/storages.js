import { http } from '@/api/http'

export const storagePresignedURL = (data) =>
  http.post('/storages/presigned-url/', data)
