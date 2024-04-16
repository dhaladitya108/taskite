from django.db import models
from django.utils.text import slugify

from taskite.models.base import BaseTimestampModel


class Project(BaseTimestampModel):
    class Visibility(models.TextChoices):
        PRIVATE = ("private", "Private")
        PUBLIC = ("public", "Public")
        INTERNAL = ("internal", "Internal")

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=125, unique=True, blank=True)
    project_id = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True, null=True)
    visibility = models.CharField(
        max_length=10, choices=Visibility.choices, default=Visibility.PRIVATE
    )
    created_by = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)

    members = models.ManyToManyField(
        "User",
        through="ProjectMember",
        related_name="projects",
        related_query_name="project",
    )

    class Meta:
        db_table = "projects"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.slug:
                self.slug = slugify(self.name.lower)
            if not self.project_id:
                self.project_id = self.generate_project_id()
        super().save(*args, **kwargs)

    def generate_project_id(self):
        # Remove all characters except alphanumeric and spaces.
        clean_text = "".join(
            char for char in self.name.lower() if char.isalnum() or char.isspace()
        )

        # Split the text into words.
        words = clean_text.strip().split()

        # Take the first letter of each word (if available) and combine them in uppercase.
        slug = "".join(word[0] for word in words if word)

        # If the slug is empty, use the first two characters of the original text.
        if not slug:
            slug = self.name[:2].upper()

        # Limit the slug length to 4 characters (can be adjusted as needed).
        return slug[:4].upper()


class ProjectMember(BaseTimestampModel):
    class Role(models.TextChoices):
        ADMIN = ("admin", "Admin")
        MEMBER = ("member", "Member")
        GUEST = ("guest", "Guest")

    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        related_name="project_members",
        related_query_name="project_member",
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="user_projects",
        related_query_name="user_project",
    )
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.MEMBER)

    class Meta:
        db_table = "project_members"
        verbose_name = "Project Member"
        verbose_name_plural = "Project Members"
        ordering = ("-created_at",)
        constraints = [
            models.UniqueConstraint(
                name="unique_project_members", fields=["project_id", "user_id"]
            )
        ]

    def __str__(self) -> str:
        return f"{self.id}"
