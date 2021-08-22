import uuid

from django.db import models


class AbstractBaseModel(models.Model):
    class Meta:
        abstract = True

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    datetime_created = models.DateTimeField(auto_now_add=True, editable=False)
    datetime_modified = models.DateTimeField(auto_now=True, editable=False)