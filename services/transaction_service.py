from datetime import datetime

from models.transaction import Transaction

from repositories.wallet_repository import WalletRepository
from repositories.customer_repository import CustomerRepository
from repositories.transaction_repository import TransactionRepository

class TransactionService:
    def __init__(self,transaction_repository,wallet_repository):
        self.transaction_repository=transaction_repository
        self.wallet_repository=wallet_repository
        
    def create_transaction(self,sender_wallet_id,receiver_wallet_id,amount,transaction_type,status,created_at):
        transaction_obj=Transaction(
            sender_wallet_id=sender_wallet_id,
            receiver_wallet_id=receiver_wallet_id,
            amount=amount,
            transaction_type=transaction_type,
            status=status,
            created_at=created_at
        )
        self.transaction_repository.add_transaction(transaction_obj)
        
        return transaction_obj
        
    
    def transfer_money(self,sender_number,receiver_number,amount):
        sender_wallet_obj=self.wallet_repository.get_wallet_by_number(sender_number)
        receiver_wallet_obj=self.wallet_repository.get_wallet_by_number(receiver_number)
        
        if sender_wallet_obj is None:
            raise ValueError("Entered number is not registered yet")
        if receiver_wallet_obj is None:
            raise ValueError("The entered receiver number does not exist")
        
        
        sender_wallet_obj.withdraw_money(amount)
        receiver_wallet_obj.add_balance(amount)

        
        self.wallet_repository.update_balance(sender_wallet_obj.wallet_id,sender_wallet_obj.balance)
        self.wallet_repository.update_balance(receiver_wallet_obj.wallet_id,receiver_wallet_obj.balance)
        
        return self.create_transaction(
            sender_wallet_obj.wallet_id,
            receiver_wallet_obj.wallet_id,
            amount=amount,
            transaction_type="Transfer",
            status="Success",
            created_at=datetime.now()
            
        )

        
        
        