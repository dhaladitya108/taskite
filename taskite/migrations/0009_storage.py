# Generated by Django 5.0.4 on 2024-05-04 12:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskite", "0008_user_avatar_projectmemberinvite"),
    ]

    operations = [
        migrations.CreateModel(
            name="Storage",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("filename", models.CharField(max_length=225, unique=True)),
                ("uploaded_at", models.DateTimeField(blank=True, null=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "storages",
            },
        ),
    ]
