# Generated by Django 3.1.7 on 2021-04-14 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_models', '0003_walletwithdraw'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WalletAdjust',
        ),
    ]