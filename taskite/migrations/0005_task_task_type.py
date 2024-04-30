# Generated by Django 5.0.4 on 2024-04-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskite", "0004_project_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="task_type",
            field=models.CharField(
                choices=[
                    ("issue", "Issue"),
                    ("task", "Task"),
                    ("bug", "Bug"),
                    ("epic", "Epic"),
                    ("story", "Story"),
                ],
                default="task",
                max_length=10,
            ),
        ),
    ]