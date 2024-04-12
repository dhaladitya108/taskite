from django.db import models


class BaseTimestampModel(models.Model):
    # BigInt - ID as primary key
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
