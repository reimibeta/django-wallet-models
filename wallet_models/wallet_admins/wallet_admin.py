from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter


# wallet change
from ..wallet_models.wallet import Wallet
from ..wallet_models.wallet_change import WalletChange


class WalletChangeAdmin(admin.ModelAdmin):
    list_display = [
        'wallet',
        'amount',
        'note',
        'created_date'
    ]
    list_display_links = [
        'wallet',
    ]
    list_per_page = 25

    list_filter = (
        # for ordinary fields
        # ('wallet', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('wallet', RelatedDropdownFilter),
    )
    search_fields = [
        'wallet',
    ]

    # def money(self, obj):
    #     return "{} {}".format(
    #         obj.currency.currency if obj.currency is not None else 'not provided',
    #         obj.balance
    #     )
    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(WalletChange, WalletChangeAdmin)


# wallet
class WalletAdmin(admin.ModelAdmin):
    list_display = [
        'wallet',
        'user',
        'money',
        'created_date',
        'updated_date'
    ]
    list_display_links = [
        'wallet',
        'user'
    ]
    list_per_page = 25

    list_filter = (
        # for ordinary fields
        ('wallet', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('user', RelatedDropdownFilter),
    )
    search_fields = [
        'wallet',
    ]

    def money(self, obj):
        return "{} {}".format(
            obj.balance,
            obj.currency.currency if obj.currency is not None else 'not provided'
        )


admin.site.register(Wallet, WalletAdmin)
