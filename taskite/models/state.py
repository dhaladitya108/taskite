from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from taskite.models.base import BaseUUIDTimestampModel
from taskite.models.project import Project


class State(BaseUUIDTimestampModel):
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="states"
    )
    name = models.CharField(max_length=125)
    order = models.FloatField(editable=False, blank=True)
    color = models.CharField(max_length=10, default="#33cc33")

    class Meta:
        db_table = "states"
        ordering = ("order",)

    def __str__(self):
        return f"{self.name} <{self.id}>"

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.order:
                last_id = (
                    State.objects.filter(project=self.project)
                    .aggregate(largest=models.Max("order"))
                    .get("largest")
                )
                if last_id is not None:
                    self.order = last_id + 1000
                else:
                    self.order = 5000
        return super().save(*args, **kwargs)

    @receiver(post_save, sender=Project)
    def add_default_project_states(sender, created, instance, **kwargs):
        if created:
            State.objects.bulk_create(
                [
                    State(project=instance, name="Backlog", order=50000),
                    State(project=instance, name="Todo", order=60000),
                    State(project=instance, name="Progress", order=70000),
                    State(project=instance, name="Done", order=80000),
                    State(project=instance, name="Cancelled", order=90000)
                ]
            )