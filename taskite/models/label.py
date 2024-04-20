from django.db import models

from taskite.models.base import BaseUUIDTimestampModel


class Label(BaseUUIDTimestampModel):
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="labels"
    )
    name = models.CharField(max_length=124)
    color = models.CharField(max_length=10, default="#33cc33")

    class Meta:
        db_table = "labels"
        constraints = [
            models.UniqueConstraint(
                fields=["project_id", "name"], name="unique_project_label_name"
            )
        ]

    def __str__(self) -> str:
        return f"{self.name} <{self.id}>"
