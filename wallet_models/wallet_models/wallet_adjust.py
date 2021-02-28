from decimal import Decimal

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime_utils.date_time import DateTime
from ..wallet_models.wallet import Wallet


class WalletAdjust(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=Decimal(0.00),
        blank=True,
        null=True
    )
    created_date = models.DateField(default=DateTime.datenow)

    def __str__(self):
        return "{}".format(self.wallet)


@receiver(post_save, sender=WalletAdjust)
def add(sender, instance, created, **kwargs):
    if created:
        wallet = Wallet.objects.get(id=instance.wallet.id)
        if wallet:
            wallet.balance = instance.amount
        wallet.save()

# @receiver(pre_save, sender=WalletAdjust)
# def update(sender, instance, **kwargs):
#     if instance is None:
#         pass
#     else:
#         if instance.created_date is None:
#             instance.created_date = DateTime.datenow()
#         # wallet
#         wallet = Wallet.objects.get(id=instance.wallet.id)
#         if wallet:
#             wallet.balance = instance.amount
#         wallet.save()


# @receiver(post_delete, sender=OrderProduct)
# def delete(sender, instance, using, **kwargs):
#     pass
