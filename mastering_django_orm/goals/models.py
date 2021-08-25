import decimal

from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import DateRangeField, RangeBoundary, RangeOperators
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mastering_django_orm.organizations.mixins import OrganizationModelMixin


class DateRangeFunc(models.Func):
    function = "daterange"
    output_field = DateRangeField()


class SubjectiveGoal(OrganizationModelMixin):
    class Meta:
        verbose_name = "Subjective Goal"
        verbose_name_plural = "Subjective Goals"
        constraints = [
            ExclusionConstraint(
                name="exclude_overlapping_subjective_goals",
                expressions=(
                    (
                        DateRangeFunc("start_date", "end_date", RangeBoundary()),
                        RangeOperators.OVERLAPS,
                    ),
                    ("employee", RangeOperators.EQUAL),
                    ("organization", RangeOperators.EQUAL),
                ),
            ),
            models.CheckConstraint(
                name="baseline_less_than_target",
                check=models.Q(baseline__lte=models.F("target")),
            ),
        ]

    name = models.CharField(max_length=255)
    employee = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="subjective_goals",
    )
    target = models.DecimalField(
        _("Target"),
        decimal_places=2,
        max_digits=3,
        validators=[
            MinValueValidator(decimal.Decimal(1)),
            MaxValueValidator(decimal.Decimal(5)),
        ],
    )
    baseline = models.DecimalField(
        _("Baseline"),
        decimal_places=2,
        max_digits=3,
        default=decimal.Decimal("2.50"),
        validators=[
            MinValueValidator(decimal.Decimal(1)),
            MaxValueValidator(decimal.Decimal(5)),
        ],
    )
    start_date = models.DateTimeField(_("Goal Start Date"))
    end_date = models.DateTimeField(_("Goal End Date"))

    def __str__(self):
        return f"{self.employee} Goal {self.name}"
