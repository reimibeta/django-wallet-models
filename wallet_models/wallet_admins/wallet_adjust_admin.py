from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from ..wallet_models.wallet_adjust import WalletAdjust


class WalletAdjustAdmin(admin.ModelAdmin):
    list_display = [
        'wallet',
        'money',
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

    def money(self, obj):
        return "{} {}".format(
            obj.amount,
            obj.wallet.currency.currency if obj.wallet.currency is not None else 'not provided'
        )

    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(WalletAdjust, WalletAdjustAdmin)
