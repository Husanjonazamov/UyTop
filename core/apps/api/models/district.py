from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class DistrictModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "District"
        verbose_name = _("DistrictModel")
        verbose_name_plural = _("DistrictModels")
