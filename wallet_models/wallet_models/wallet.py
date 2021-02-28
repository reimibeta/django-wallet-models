from decimal import Decimal
from django.conf import settings
# from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from datetime_utils.date_time import DateTime
from ..wallet_models.wallet_currency import WalletCurrency


class Wallet(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    wallet = models.CharField(max_length=160)
    currency = models.ForeignKey(WalletCurrency, on_delete=models.CASCADE)
    balance = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=Decimal(0.00),
        blank=True,
        null=True
    )
    created_date = models.DateField(default=DateTime.datenow)
    updated_date = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'wallet')
        verbose_name = 'Wallets'
        verbose_name_plural = 'Wallets'

    def __str__(self):
        return '{} ({})'.format(self.wallet, self.currency.currency)


# @receiver(post_save, sender=OrderProduct)
# def add(sender, instance, created, **kwargs):
#     pass


# @receiver(post_save, sender=OrderProduct)
# def post_update(sender, instance, **kwargs):
#     pass


@receiver(pre_save, sender=Wallet)
def update(sender, instance, **kwargs):
    if instance is None:
        pass
    else:
        if instance.updated_date is None:
            instance.updated_date = DateTime.datenow()

# @receiver(post_delete, sender=OrderProduct)
# def delete(sender, instance, using, **kwargs):
#     pass
