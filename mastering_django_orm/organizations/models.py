from django.conf import settings
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

    def __str__(self):
        return self.name


class OrganizationUser(AbstractBaseModel):
    class Meta:
        verbose_name = "Organization User"
        verbose_name_plural = "Organization Users"
        constraints = [models.UniqueConstraint(fields=["organization", "user"], name="unique_org_user")]

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="organization_users")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="organization_users",
        on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} {self.organization}"
