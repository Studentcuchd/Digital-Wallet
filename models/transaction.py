class Transaction:
    def __init__(self,sender_wallet_id,receiver_wallet_id,amount,transaction_type,status,created_at,transaction_id=None):
        self.sender_wallet_id=sender_wallet_id
        self.receiver_wallet_id=receiver_wallet_id
        self.amount=amount
        self.transaction_type=transaction_type
        self.status=status
        self.created_at=created_at
        self.transaction_id=transaction_id