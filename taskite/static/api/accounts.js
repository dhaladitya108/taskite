import { http } from '@/api/http'

export const loginAPI = (data) => http.post('/accounts/login/', data)

export const registerAPI = (data) => http.post('/accounts/register/', data)

export const profileUpdateAPI = (data) => http.patch('/accounts/profile/', data)