from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mastering_django_orm.core.mixins import AbstractBaseModel
from mastering_django_orm.organizations.models import Organization


class User(AbstractBaseModel, AbstractUser):
    name = models.CharField(_("Name"), max_length=254)
    organizations = models.ManyToManyField(Organization, through="organizations.OrganizationUser")
    date_joined = None
    first_name = None
    last_name = None

    def __str__(self):
        return f"{self.name} {self.email}"
