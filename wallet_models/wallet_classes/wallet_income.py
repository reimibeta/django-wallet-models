from wallet_models.wallet_classes.wallet_base import WalletAccountBase


class WalletAccountIncome:
    @classmethod
    def income_account(cls, amount, account_pk):
        account = WalletAccountBase(account_pk)
        account.income_account_balance(
            account.balance, amount
        )

    @classmethod
    def update_income_account(cls, new_amount, old_amount, account_pk):
        account = WalletAccountBase(account_pk)
        account.update_income_account_balance(
            account.balance, new_amount, old_amount
        )

    @classmethod
    def return_income_account(cls, amount, account_pk):
        account = WalletAccountBase(account_pk)
        account.return_income_account_balance(
            account.balance, amount
        )