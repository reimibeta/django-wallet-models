# Generated by Django 3.1.7 on 2021-03-03 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_models', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WalletChange',
            new_name='WalletInsert',
        ),
    ]
