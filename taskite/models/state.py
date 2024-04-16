from typing import Iterable
from django.db import models

from taskite.models.base import BaseTimestampModel


class State(BaseTimestampModel):
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="states"
    )
    name = models.CharField(max_length=125)
    order = models.FloatField(default=50000, editable=False, blank=True)
    color = models.CharField(max_length=10, default="#33cc33")

    class Meta:
        db_table = "states"
        ordering = ("order",)

    def __str__(self):
        return f"{self.name} <{self.id}>"

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id = (
                State.objects.filter(project=self.project)
                .aggregate(largest=models.Max("order"))
                .get("largest")
            )
            if last_id is not None:
                self.order = last_id + 10000
        return super().save(*args, **kwargs)
