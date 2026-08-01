from datetime import datetime

from models.transaction import Transaction

from repositories.wallet_repository import WalletRepository

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
        
        try:
        
            sender_wallet_obj.withdraw_money(amount)
            receiver_wallet_obj.add_balance(amount)

        
            self.wallet_repository.update_balance(sender_wallet_obj.wallet_id,sender_wallet_obj.balance)
            self.wallet_repository.update_balance(receiver_wallet_obj.wallet_id,receiver_wallet_obj.balance)
            
       
            transaction= self.create_transaction(
                sender_wallet_obj.wallet_id,
                receiver_wallet_obj.wallet_id,
                amount=amount,
                transaction_type="Transfer",
                status="Success",
                created_at=datetime.now()
            )
            self.wallet_repository.database.commit()
            return transaction
                    
        except Exception:
            self.wallet_repository.database.rollback()
            raise 
        
        
    def make_payment(self,sender_number,receiver_number,amount):
        sender_wallet_obj=self.wallet_repository.get_wallet_by_number(sender_number)
        receiver_wallet_obj=self.wallet_repository.get_wallet_by_number(receiver_number)
        
        if sender_wallet_obj is None:
            raise ValueError("Entered number is not registered yet")
        if receiver_wallet_obj is None:
            raise ValueError("The entered receiver number does not exist")
        
        try:
        
            sender_wallet_obj.withdraw_money(amount)
            receiver_wallet_obj.add_balance(amount)

        
            self.wallet_repository.update_balance(sender_wallet_obj.wallet_id,sender_wallet_obj.balance)
            self.wallet_repository.update_balance(receiver_wallet_obj.wallet_id,receiver_wallet_obj.balance)
            
       
            transaction= self.create_transaction(
                sender_wallet_obj.wallet_id,
                receiver_wallet_obj.wallet_id,
                amount=amount,
                transaction_type="Payment",
                status="Success",
                created_at=datetime.now()
            )
            cashback=self.add_cashback(transaction)
            
            self.wallet_repository.database.commit()
            return transaction,cashback
                    
        except Exception:
            self.wallet_repository.database.rollback()
            raise 

    
    def get_spending_summary(self,mobile_number):
        wallet_obj=self.wallet_repository.get_wallet_by_number(mobile_number)
        if wallet_obj is None:
            raise ValueError("No wallet exist for this mobile number")
        
        return self.transaction_repository.get_spend_summary(wallet_obj.wallet_id)
    
    
    def add_cashback(self,transaction_makepayment_obj):
            
        if transaction_makepayment_obj.amount>=300:
            cashback=min((transaction_makepayment_obj.amount)//10,100)
            balance=self.wallet_repository.get_balance(transaction_makepayment_obj.sender_wallet_id)
            balance+=cashback
            self.wallet_repository.update_balance(transaction_makepayment_obj.sender_wallet_id,balance)
            return cashback   

        return 0
        
    def get_transaction_history(self, mobile_number):
        wallet_obj = self.wallet_repository.get_wallet_by_number(mobile_number)

        if wallet_obj is None:
            raise ValueError("No wallet exists for this mobile number")

        return self.transaction_repository.get_all_transaction(wallet_obj.wallet_id)       
        
        