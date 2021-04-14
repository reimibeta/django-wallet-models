from wallet_models.wallet_classes.wallet_base import WalletAccountBase


class WalletAccountOutlet:

    @classmethod
    def outlet_account(cls, amount, account_pk):
        account = WalletAccountBase(account_pk)
        account.outlet_account_balance(
            account.balance, amount
        )

    @classmethod
    def update_outlet_account(cls, new_amount, old_amount, account_pk):
        account = WalletAccountBase(account_pk)
        account.update_outlet_account_balance(
            account.balance, new_amount, old_amount
        )

    @classmethod
    def refund_outlet_account(cls, amount, account_pk):
        account = WalletAccountBase(account_pk)
        if account:
            account.return_outlet_account_balance(
                account.balance, amount
            )
