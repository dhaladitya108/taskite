import json
import random
from taskite.models import User, Project, ProjectMember, State, Task, TaskAssignee

project = Project.objects.filter(slug="prime-siliconite").first()

users = User.objects.filter()

# for user in users:
#     try:
#         ProjectMember.objects.create(project=project, user=user)
#     except:
#         print('Unable to create project member.')

states = State.objects.filter(project=project)


file = open('tasks.json', 'r')

tasks = json.load(file)

for t in tasks:
    state = states[random.randint(0, len(states) - 1)]
    task = Task.objects.create(project=project, name=t["title"], description=t["description"], state=state)

    member_count = random.randint(1, 5)
    for _ in range(member_count):
        random_user = users[random.randint(0, len(users) - 1)]
        try:
            TaskAssignee.objects.create(user=random_user, task=task)
        except:
            print('Unable to add task assignee')