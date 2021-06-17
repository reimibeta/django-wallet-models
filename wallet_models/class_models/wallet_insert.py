from decimal import Decimal

from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

from django_datetime.datetime import datetime

from wallet_models.class_models.wallet import Wallet
from wallet_models.class_apps.wallets.wallet_income import WalletAccountIncome


class WalletInsert(models.Model):
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


@receiver(post_save, sender=WalletInsert)
def add(sender, instance, created, **kwargs):
    if created:
        WalletAccountIncome.income_account(
            instance.amount,
            instance.wallet.id
        )


@receiver(pre_save, sender=WalletInsert)
def update(sender, instance, **kwargs):
    if instance.id is None:
        pass
    else:
        if instance.updated_date is None:
            instance.updated_date = datetime.dnow()
        old_value = WalletInsert.objects.get(id=instance.id)
        WalletAccountIncome.update_income_account(
            instance.amount,
            old_value.amount,
            instance.wallet.id
        )


@receiver(pre_delete, sender=WalletInsert)
def delete(sender, instance, using, **kwargs):
    old_value = WalletInsert.objects.get(id=instance.id)
    WalletAccountIncome.return_income_account(
        old_value.amount,
        old_value.wallet.id
    )
