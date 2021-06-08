from decimal import Decimal

from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers

from wallet_models.class_models.wallet import Wallet
from user_models.class_serializers.user_serializers import UserSerializer

from wallet_models.class_models.wallet_currency import WalletCurrency


class WalletSerializer(FlexFieldsModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    # order_build_workers = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    currency = serializers.PrimaryKeyRelatedField(
        queryset=WalletCurrency.objects.all(),
        write_only=True
    )

    balance = serializers.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=Decimal(0.00),
        write_only=True
    )

    balance_available = serializers.SerializerMethodField('balance_available_define')

    def balance_available_define(self, obj):
        return "{} {}".format(obj.balance, obj.currency.currency)

    class Meta:
        model = Wallet
        # exclude = ('removed_by',)
        fields = [
            'id',
            'url',
            'user',
            'wallet',
            'currency',
            'balance',
            'balance_available',
            'created_date',
            'updated_date',
        ]
        expandable_fields = {
            'user': UserSerializer,
        }
