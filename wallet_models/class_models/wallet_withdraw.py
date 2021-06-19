from decimal import Decimal

from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

from django_datetime.datetime import datetime

from wallet_models.class_models.wallet import Wallet
from wallet_models.class_apps.wallets.wallet_outlet import WalletAccountOutlet


class WalletWithdraw(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=Decimal(0.00),
        blank=True,
        null=True
    )
    note = models.CharField(max_length=250, blank=True, null=True)
    created_date = models.DateField(default=datetime.dnow())
    updated_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.wallet)


@receiver(post_save, sender=WalletWithdraw)
def add(sender, instance, created, **kwargs):
    if created:
        WalletAccountOutlet.outlet_account(
            instance.amount,
            instance.wallet.id
        )


@receiver(pre_save, sender=WalletWithdraw)
def update(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        if instance.updated_date is None:
            instance.updated_date = datetime.dnow(str=True)

        old_value = WalletWithdraw.objects.get(id=instance.id)
        WalletAccountOutlet.update_outlet_account(
            instance.amount,
            old_value.amount,
            instance.wallet.id
        )


@receiver(pre_delete, sender=WalletWithdraw)
def delete(sender, instance, using, **kwargs):
    old_value = WalletWithdraw.objects.get(id=instance.id)
    WalletAccountOutlet.refund_outlet_account(
        old_value.amount,
        old_value.wallet.id
    )
