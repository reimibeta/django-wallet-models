from wallet_models.class_apps.wallets.wallet_income import WalletAccountIncome


class BalanceIncome:
    @staticmethod
    def income(amount, account_pk):
        WalletAccountIncome.income_account(
            amount, account_pk
        )

    @staticmethod
    def update(new_amount, old_amount, account_pk):
        WalletAccountIncome.update_income_account(
            new_amount, old_amount, account_pk
        )

    @staticmethod
    def refund(amount, account_pk):
        WalletAccountIncome.return_income_account(
            amount, account_pk
        )
