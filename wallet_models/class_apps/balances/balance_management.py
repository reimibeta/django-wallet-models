from wallet_models.class_apps.balances.outlets.balance_outlet_condition import balance_outlet_condition


class LendingAmountManagement:

    # def __init__(self, condition):
    #     self.condition = condition

    def lend_money(self, current_instance, current_amount):
        balance_outlet_condition.set_current_pk(current_instance.account.id)
        balance_outlet_condition.set_current_condition(current_instance.is_return)
        balance_outlet_condition.outlet_account(current_amount)

    def lend_update(self, current_instance, last_instance, current_amount, last_amount):
        balance_outlet_condition.set_current_pk(current_instance.account.id)
        balance_outlet_condition.set_current_condition(current_instance.is_return)
        balance_outlet_condition.set_last_pk(last_instance.account.id)
        balance_outlet_condition.set_last_condition(last_instance.is_return)
        balance_outlet_condition.update_outlet_account(
            current_amount=current_amount,
            last_amount=last_amount
        )

    def lend_return(self, last_instance, last_amount):
        balance_outlet_condition.set_last_condition(last_instance.is_return)
        balance_outlet_condition.set_last_pk(last_instance.account.id)
        balance_outlet_condition.refund_outlet_account(last_amount=last_amount)


lending_amount_management = LendingAmountManagement()
