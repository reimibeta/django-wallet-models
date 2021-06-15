from wallet_models.class_apps.balances.incomes.balance_income_condition import balance_income_condition
from wallet_models.class_apps.balances.objects.instance_base import CurrentInstance, LastInstance


class BalanceIncome(CurrentInstance):

    def __init__(
            self,
            current_condition,
            current_instance,
            current_amount
    ):

        CurrentInstance.__init__(
            self,
            current_condition, current_instance, current_amount
        )

    def income(self):
        if not self.current_instance:
            raise ValueError('Current instance must set.')
        balance_income_condition.set_current_pk(
            self.current_instance.account.id
        )
        if not self.current_condition:
            raise ValueError('Current condition must set.')
        balance_income_condition.set_current_condition(
            self.current_condition
        )
        if not self.current_amount:
            raise ValueError('Current amount must set.')
        balance_income_condition.income_account(
            self.current_amount
        )


class BalanceRefund(LastInstance):

    def __init__(
            self,
            last_condition,
            last_instance,
            last_amount
    ):
        LastInstance.__init__(
            self,
            last_condition,
            last_instance,
            last_amount
        )

    def refund(self):
        if not self.last_condition:
            raise ValueError('Last condition must set.')
        balance_income_condition.set_last_condition(self.last_condition)
        if not self.last_instance:
            raise ValueError('Last instance must set.')
        balance_income_condition.set_last_pk(self.last_instance.account.id)
        if not self.last_amount:
            raise ValueError('Last amount must set.')
        balance_income_condition.refund_income_account(
            last_amount=self.last_amount
        )


class BalanceUpdate(CurrentInstance, LastInstance):

    def __init__(
            self,
            current_condition,
            current_instance,
            current_amount,
            last_condition,
            last_instance,
            last_amount
    ):
        CurrentInstance.__init__(
            self,
            current_condition,
            current_instance,
            current_amount
        )
        LastInstance.__init__(
            self,
            last_condition,
            last_instance,
            last_amount
        )

    def update(self):
        if not self.current_amount:
            raise ValueError('Current amount must set.')
        balance_income_condition.set_current_pk(self.current_instance.account.id)
        if not self.current_condition:
            raise ValueError('Current condition must set.')
        balance_income_condition.set_current_condition(self.current_condition)
        if not self.last_instance:
            raise ValueError('Last instance must set.')
        balance_income_condition.set_last_pk(self.last_instance.account.id)
        if not self.last_condition:
            raise ValueError('Last condition must set.')
        balance_income_condition.set_last_condition(self.last_condition)
        if not self.current_amount and self.last_amount:
            raise ValueError('Current amount and last amount must set.')
        balance_income_condition.update_income_account(
            current_amount=self.current_amount,
            last_amount=self.last_amount
        )
