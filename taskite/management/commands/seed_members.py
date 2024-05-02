from django.core.management.base import BaseCommand, CommandError
from taskite.models import Project, User, Task, TaskAssignee, State, Label, TaskLabel, ProjectMember
from faker import Faker
from django.utils.text import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("project_slug", type=str, help="Project slug")
        parser.add_argument("member_count", type=int, help="No of members")

    def handle(self, *args, **options):
        project = Project.objects.filter(slug=options["project_slug"]).first()
        if not project:
            raise CommandError("Project doesn't exist with given project slug.")
        
        member_count = options["member_count"]
        
        for i in range(member_count):
            fake = Faker()
            name = fake.name()
            username = name.split(" ")[0].lower()
            user = User(full_name=name, email=f"{slugify(name.lower())}@acornglobus.com", username=username)
            user.set_password('password')
            user.save()
            ProjectMember.objects.create(user=user, project=project)