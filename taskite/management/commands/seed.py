import random
from django.core.management.base import BaseCommand, CommandError
from taskite.models import Project, User, Task, TaskAssignee, State, Label, TaskLabel
from faker import Faker

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("project_slug", type=str, help="Project slug")
        parser.add_argument("task_count", type=int, help="No of task count")

    def handle(self, *args, **options):
        project = Project.objects.filter(slug=options["project_slug"]).first()
        if not project:
            raise CommandError("Project doesn't exist with given project slug.")
        
        task_count = options["task_count"]
        
        fake = Faker()
        members = User.objects.filter(user_project__project=project)
        labels = Label.objects.filter(project=project)
        states = State.objects.filter(project=project)
        priorities = ["urgent", "high", "low", "medium"]
        task_types = ["epic", "issue", "bug", "story"]

        for i in range(task_count):
            task = Task.objects.create(
                state=random.choice(states),
                project=project, 
                name=fake.text(), 
                description=fake.text(), 
                priority=random.choice(priorities),
                task_type=random.choice(task_types)
            )
            for _ in range(random.randint(0, 7)):
                try:
                    TaskAssignee.objects.create(task=task, user=random.choice(members))
                except Exception:
                    self.stdout.write(
                        self.style.WARNING("Exception occured while creating task assignees")
                    )

            for _ in range(random.randint(0, 3)):
                try:
                    TaskLabel.objects.create(task=task, label=random.choice(labels))
                except Exception:
                    self.stdout.write(
                        self.style.WARNING("Exception occured while creating task labels")
                    )