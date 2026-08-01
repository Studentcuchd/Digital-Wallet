from models.wallet import Wallet

from repositories.customer_repository import CustomerRepository
from repositories.wallet_repository import WalletRepository
from services.coupon_service import CouponService

class WalletService:
    
    def __init__(self,wallet_repository,customer_repository,coupon_service):
        self.wallet_repository=wallet_repository
        self.customer_repository=customer_repository
        self.coupon_service=coupon_service
        
    
    
    def add_wallet(self,mobile_number):
        customer_id=self.customer_repository.get_customer_id_by_number(mobile_number)
        
        if customer_id is None:
            raise ValueError(f"user not found please register yurself firstly")
        
        wallet_obj=Wallet(
            customer_id=customer_id,
            balance=0
        )
        
        self.wallet_repository.create_wallet(wallet_obj) 
        self.coupon_service.generate_coupon(wallet_obj.wallet_id)
        return wallet_obj
           
        
    
    def add_money(self,mobile_number,amount):
        wallet_obj=self.wallet_repository.get_wallet_by_number(mobile_number)
        
        if wallet_obj is None:
            raise ValueError("Your wallet is not created yet please create your wallet")
        
        wallet_obj.add_balance(amount)
        
        self.wallet_repository.update_balance(wallet_obj.wallet_id,wallet_obj.balance)
        
    
    def get_balance(self,mobile_number):
        wallet_obj=self.wallet_repository.get_wallet_by_number(mobile_number)
        
        if wallet_obj is None:
            raise ValueError("You donot have any wallet for this mobile number")
        
        return wallet_obj.balance
    
        
        
