# Generated by Django 5.0.4 on 2024-05-15 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskite", "0023_alter_storage_options_project_theme_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectmember",
            name="invited_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="projectmember",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]