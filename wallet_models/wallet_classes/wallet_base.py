from wallet_models.wallet_models.wallet import Wallet


class WalletAccountBase:
    account = None
    balance = None

    def __init__(self, account_id):
        self.account = Wallet.objects.get(id=account_id)
        if self.account:
            self.balance = self.account.balance
        else:
            print('account model not found!')

    def outlet_account_balance(self, balance, amount):
        self.account.balance = balance - amount
        self.account.save()

    def income_account_balance(self, balance, amount):
        self.account.balance = balance + amount
        self.account.save()

    def update_outlet_account_balance(self, balance, new_amount, old_amount):
        self.account.balance = balance + old_amount - new_amount
        self.account.save()

    def update_income_account_balance(self, balance, new_amount, old_amount):
        self.account.balance = balance - old_amount + new_amount
        self.account.save()

    def return_outlet_account_balance(self, balance, amount):
        self.account.balance = balance + amount
        self.account.save()

    def return_income_account_balance(self, balance, amount):
        self.account.balance = balance - amount
        self.account.save()