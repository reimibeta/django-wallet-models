from decimal import Decimal

from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver

from datetime_utils.date_time import DateTime

from ..wallet_classes.wallet_management import WalletAccountIncome
from ..wallet_models.wallet import Wallet


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
    created_date = models.DateField(default=DateTime.datenow)
    updated_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.wallet)


@receiver(post_save, sender=WalletInsert)
def add(sender, instance, created, **kwargs):
    if created:
        # wallet = Wallet.objects.get(id=instance.wallet.id)
        # if wallet:
        #     wallet.balance = wallet.balance + instance.amount
        # wallet.save()
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
            instance.updated_date = DateTime.datenow()
        # wallet = Wallet.objects.get(id=instance.wallet.id)
        # if wallet:
        #     old_record = WalletInsert.objects.get(id=instance.id)
        #     if old_record:
        #         wallet.balance = wallet.balance - old_record.amount + instance.amount
        # wallet.save()
        old_value = WalletInsert.objects.get(id=instance.id)
        WalletAccountIncome.update_income_account(
            instance.amount,
            old_value.amount,
            instance.wallet.id
        )


@receiver(pre_delete, sender=WalletInsert)
def delete(sender, instance, using, **kwargs):
    # wallet = Wallet.objects.get(id=instance.wallet.id)
    # print(instance.id)
    # if wallet:
    #     # old_record = Expense.objects.get(id=instance.id)
    #     # if old_record:
    #     wallet.balance = wallet.balance - instance.amount
    # wallet.save()
    old_value = WalletInsert.objects.get(id=instance.id)
    WalletAccountIncome.return_income_account(
        old_value.amount,
        old_value.wallet.id
    )