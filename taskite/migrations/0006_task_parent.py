# Generated by Django 5.0.4 on 2024-04-27 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskite", "0005_task_task_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="taskite.task",
            ),
        ),
    ]
