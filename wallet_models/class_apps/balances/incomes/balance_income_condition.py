# from wallet_models.class_apps.balances.incomes.balance_income import BalanceIncome
from wallet_models.class_apps.balances.objects.object_base import SetObjectPk, SetObjectCondition
from wallet_models.class_apps.wallets.wallet_income import WalletAccountIncome


class BalanceIncomeCondition(SetObjectPk, SetObjectCondition):

    def income_account(self, current_amount):
        if self.current_condition:
            WalletAccountIncome.income_account(current_amount, self.current_pk)

    # update
    def _update_income_account_same_pk(self, current_amount, last_amount):
        if self.current_condition:
            if self.last_condition:
                WalletAccountIncome.update_income_account(
                    current_amount, last_amount,
                    self.current_pk
                )
                # print("update amount")
            else:
                WalletAccountIncome.income_account(
                    current_amount,
                    self.current_pk
                )
        else:
            if self.last_condition:
                WalletAccountIncome.return_income_account(last_amount, self.last_pk)

    def _update_income_account_different_pk(self, current_amount, last_amount):
        if self.current_condition:
            if self.last_condition:
                # return stock
                WalletAccountIncome.return_income_account(last_amount, self.last_pk)
                # add new stock
                WalletAccountIncome.income_account(current_amount, self.current_pk)
                print('update not workings')
            else:
                WalletAccountIncome.income_account(current_amount, self.current_pk)
        else:
            if self.last_condition:
                WalletAccountIncome.return_income_account(last_amount, self.last_pk)

    def update_income_account(self, current_amount, last_amount):
        if self.current_pk == self.last_pk:
            self._update_income_account_same_pk(current_amount, last_amount)
            print('update same pk: {}'.format(self.current_pk))
            print('update current condition: {}'.format(self.current_condition))
            print('update last condition: {}'.format(self.last_condition))
        else:
            self._update_income_account_different_pk(current_amount, last_amount)
            print('update different pk: {}'.format(self.last_pk))
            print('update current condition: {}'.format(self.current_condition))
            print('update last condition: {}'.format(self.last_condition))

    def refund_income_account(self, last_amount):
        if self.last_condition:
            WalletAccountIncome.return_income_account(last_amount, self.last_pk)


balance_income_condition = BalanceIncomeCondition()
