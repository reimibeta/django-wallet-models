from django.db import models


class WalletCurrency(models.Model):
    currency = models.CharField(max_length=30)
    name = models.CharField(max_length=100, blank=True, null=True)
    symbol = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.currency
