from django.db import models
from django.utils.translation import ugettext_lazy as _

from mastering_django_orm.core.mixins import AbstractBaseModel


class Organization(AbstractBaseModel):
    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    name = models.CharField(_("Name"), max_length=254)
    email = models.EmailField(_("Email"), max_length=254)
    is_active = models.BooleanField(default=True)
