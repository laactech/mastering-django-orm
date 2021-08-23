from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mastering_django_orm.organizations.mixins import OrganizationModelMixin

User = get_user_model()


class JobType(OrganizationModelMixin):
    class Meta:
        verbose_name = "Job Type"
        verbose_name_plural = "Job Types"
        constraints = [models.UniqueConstraint(fields=["name", "organization"], name="unique_job_type_name")]

    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name


class Employee(OrganizationModelMixin):
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        constraints = [models.UniqueConstraint(fields=["user", "organization"], name="unique_employee_user")]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employees")
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE, related_name="employees")
    team = models.ForeignKey(
        "employees.Team",
        on_delete=models.CASCADE,
        related_name="employees",
        null=True,
        blank=True,
    )
    age = models.PositiveSmallIntegerField(_("Age"))
    birthday = models.DateTimeField(_("Birthday"))
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Team(OrganizationModelMixin):
    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        constraints = [models.UniqueConstraint(fields=["name", "organization"], name="unique_team_name")]

    name = models.CharField(_("Name"), max_length=255)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children", blank=True, null=True)
    manager = models.ForeignKey(Employee, related_name="manager_teams", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
