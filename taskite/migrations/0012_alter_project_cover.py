# Generated by Django 5.0.4 on 2024-05-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskite", "0011_rename_thumbnail_project_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="cover",
            field=models.ImageField(
                blank=True, null=True, upload_to="projects/covers/"
            ),
        ),
    ]
