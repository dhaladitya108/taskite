# Generated by Django 5.0.4 on 2024-05-15 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskite", "0024_projectmember_invited_at_projectmember_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectmember",
            name="accepted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
