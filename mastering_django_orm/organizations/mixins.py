from django.db import models

from mastering_django_orm.core.mixins import AbstractBaseModel
from mastering_django_orm.organizations.models import Organization


class OrganizationModelMixin(AbstractBaseModel):
    class Meta:
        abstract = True

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="%(class)ss")
