import Cookies from "js-cookie";
import axios from "axios";

const csrftoken = Cookies.get("csrftoken");

export const http = axios.create({
  baseURL: "/api",
  headers: {
    "X-CSRFToken": csrftoken,
  },
});

export const loginAPI = (data) => http.post("/home/login/", data);

export const projectListAPI = () => http.get("/projects/");
export const projectMemberListAPI = (id) =>
  http.get(`/projects/${id}/members/`);

export const stateListAPI = (project_id, params) =>
  http.get(`/projects/${project_id}/states/`, {
    params: params,
  });
export const stateTaskListAPI = (project_id, id) =>
  http.get(`/projects/${project_id}/states/${id}/tasks/`);

export const taskUpdateAPI = (project_id, task_id, data, params) =>
  http.patch(`/projects/${project_id}/tasks/${task_id}/`, data, {
    params,
  });
