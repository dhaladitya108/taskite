from django.db import models

from taskite.models.base import BaseUUIDTimestampModel


class APIToken(BaseUUIDTimestampModel):
    name = models.CharField(max_length=124)
    token = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "api_tokens"