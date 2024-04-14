# Generated by Django 5.0.4 on 2024-04-14 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskite", "0005_rename_assginees_task_assignees"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskassignee",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task_assignees",
                related_query_name="task_assignee",
                to="taskite.task",
            ),
        ),
    ]
