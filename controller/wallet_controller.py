from services.wallet_service import WalletService



class WalletController:
    def __init__(self,wallet_service):
        self.wallet_service=wallet_service

    def create_wallet(self):
        mobile_number=int(input("Enter your 10 digit number="))
        
        wallet=self.wallet_service.add_wallet(mobile_number)
        print("Wallet created successfully")
        
    def add_money(self):
        mobile_number=int(input("Enter your 10 digit number="))
        amount=int(input("Enter amount to add="))
        
        self.wallet_service.add_money(mobile_number,amount)
        
    def get_balance(self):
        mobile_number=int(input("Enter your 10 digit number="))
        balance=self.wallet_service.get_balance(mobile_number)
        print(f"Your balance right now is = {balance}")