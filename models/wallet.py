class Wallet:
    def __init__(self,customer_id,balance,wallet_id=None):
        self.customer_id=customer_id
        self.balance=balance
        self.wallet_id=wallet_id
    
    
    def add_balance(self,amount):
        
        if amount<0:
            raise ValueError("You entered a negative amount please check it")
        
        elif amount>0:
            self.balance+=amount
        
        else:
            raise ValueError(f"Please enter a valid amount to add")
        
    
    def withdraw_money(self,amount):
        
        if amount<0:
            raise ValueError("You entered a negative amount please check it")
        
        elif amount>self.balance:
            raise ValueError("Insufficient balance please add money firstly")
        
        else:
            self.balance-=amount