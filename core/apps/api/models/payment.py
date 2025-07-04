from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class PaymentModel(AbstractBaseModel):
    card_number = models.CharField(verbose_name=_("Karta raqam"), max_length=50)
    card_owner = models.CharField(verbose_name=_("Karta egasi"), max_length=200)
    top_price = models.CharField(
        verbose_name=_("Top elon kunlik narxi"), max_length=100, blank=True, null=True, help_text="(1 kunlik narx)"
    )
    listing_price = models.CharField(verbose_name=_("Elon narxi"), max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.card_number)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "payment"
        verbose_name = _("PaymentModel")
        verbose_name_plural = _("PaymentModels")



class CheckModel(AbstractBaseModel):
    listing = models.ForeignKey(
        "api.ListingModel",
        verbose_name=_("Elon"),
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    
    image = models.ImageField(
        verbose_name=_("Check"),
        upload_to="check/",
        blank=True, null=True
    )
    

    def __str__(self):
        return str(self.listing.id)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "check"
        verbose_name = _("CheckModel")
        verbose_name_plural = _("CheckModels")
