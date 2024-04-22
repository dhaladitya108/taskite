from rest_framework.exceptions import APIException
from rest_framework import status


class InvalidRequestBodyAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "invalid_request_body"
    default_detail = "Invalid request body"


class ProjectNotFoundAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "project_not_found"
    default_detail = "No project found with the given project ID."


class ProjectPermissionAPIExecption(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_code = "invalid_project_permission"
    default_detail = "No you don't have enough permission to perform this action."


class TaskNotFoundAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "task_not_found"
    default_detail = "No tasks found with the given task ID."


class StateNotFoundAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "state_not_found"
    default_detail = "No tate found with the given state ID."
