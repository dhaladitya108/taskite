from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from taskite.models.base import BaseUUIDTimestampModel


class Storage(BaseUUIDTimestampModel):
    filename = models.CharField(max_length=225, unique=True)
    uploaded_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "storages"

    def __str__(self) -> str:
        return self.filename