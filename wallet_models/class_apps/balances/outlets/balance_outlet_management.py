from wallet_models.class_apps.balances.outlets.balance_outlet_condition import balance_outlet_condition


# deletable

class BalanceOutletManagement:
    # def __init__(self, condition):
    #     self.condition = condition
    condition = None
    queryset = None
    last_queryset = None

    def set_condition(self, condition):
        self.condition = condition
        return self

    def set_queryset(self, queryset):
        self.queryset = queryset
        return self

    def set_last_queryset(self, last_queryset):
        self.last_queryset = last_queryset
        return self

    def outlet(self, current_amount):
        if not self.condition:
            raise ValueError('Condition must not none.')
        balance_outlet_condition.set_current_pk(self.queryset.account.id)
        balance_outlet_condition.set_current_condition(self.condition)
        balance_outlet_condition.outlet_account(current_amount)

    def update(self, current_amount, last_amount):
        if not self.condition:
            raise ValueError('Condition must not none.')
        balance_outlet_condition.set_current_pk(self.queryset.account.id)
        balance_outlet_condition.set_current_condition(self.condition)
        balance_outlet_condition.set_last_pk(self.last_queryset.account.id)
        balance_outlet_condition.set_last_condition(self.condition)
        balance_outlet_condition.update_outlet_account(
            current_amount=current_amount,
            last_amount=last_amount
        )

    def refund(self, last_amount):
        if not self.condition:
            raise ValueError('Condition must not none.')
        balance_outlet_condition.set_last_condition(self.condition)
        balance_outlet_condition.set_last_pk(self.last_queryset.account.id)
        balance_outlet_condition.refund_outlet_account(last_amount=last_amount)


balance_outlet_management = BalanceOutletManagement()
