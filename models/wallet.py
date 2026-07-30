class Wallet:
    def __init__(self,customer_id,balance,wallet_id=None):
        self.customer_id=customer_id
        self.balance=balance
        self.wallet_id=wallet_id