from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter

from wallet_models.class_models.wallet_currency import WalletCurrency


class WalletCurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'currency', 'name', 'symbol']
    list_display_links = ['currency']
    list_per_page = 25
    list_filter = (
        # for ordinary fields
        ('currency', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        # ('currency', RelatedDropdownFilter),
    )


admin.site.register(WalletCurrency, WalletCurrencyAdmin)
