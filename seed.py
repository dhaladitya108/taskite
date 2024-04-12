import json
import random
from taskite.models import Project, Task, ProjectMember, User, TaskAssignee

f = open("data.json")

tasks = json.load(f)

project = Project.objects.get(id=1)
users = User.objects.all()
# states = project.states.all()

# print(states)

# for task in tasks:
#     index = random.randint(0, 3)
#     Task.objects.create(
#         project=project,
#         state=states[index],
#         name=task["name"],
#         description=task["description"],
#         priority=task["priority"],
#     )

# for user in User.objects.all():
#     try:
#         ProjectMember.objects.create(project=project, user=user)
#     except Exception as e:
#         print(e)

for task in Task.objects.filter(project=project):
    member_count = random.randint(1, 5)
    for i in range(member_count):
        index = random.randint(0, 25)
        try:
            TaskAssignee.objects.create(task=task, user=users[index])
        except Exception as e:
            print(e)