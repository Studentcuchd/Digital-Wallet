
from datetime import date,timedelta
from models.coupon import Coupon
from models.coupondetails import CouponDetails

from repositories.coupon_repository import CouponRepository
from repositories.wallet_repository import WalletRepository


class CouponService:
    def __init__(self,coupon_repository,wallet_repository):
        self.coupon_repository=coupon_repository
        self.wallet_repository=wallet_repository
    
    
    def generate_coupon(self,wallet_id):
        coupon_obj=Coupon(
            wallet_id,"WELCOME100",100,1000,date.today()+timedelta(days=5),0
        )
        self.coupon_repository.add_coupon(coupon_obj)
    
    
    def show_all_coupons(self,mobile_number):
        wallet_obj=self.wallet_repository.get_wallet_by_number(mobile_number)
        
        if wallet_obj is None:
            raise ValueError("No wallet exist for this numnber")

        return self.coupon_repository.get_all_coupons(wallet_obj.wallet_id)
            

    def apply_coupon(self,mobile_number,code,amount):
        wallet_obj=self.wallet_repository.get_wallet_by_number(mobile_number)
        if wallet_obj is None:
            raise ValueError("No wallet exist for this numnber")

        coupon_list=self.show_all_coupons(mobile_number)
        
        if len(coupon_list)==0:
            raise ValueError("No coupon exist right now")
        
        for coupon in coupon_list:
            
            if coupon.code==code:   
                if coupon.expired_at<str(date.today()):
                    raise ValueError("Coupon has expired already")
            
                if coupon.is_used:
                    raise ValueError("Coupon already used")
            
                if amount<coupon.minimum_amount:
                    raise ValueError("Your amount is less for this coupon") 
                
                amount=amount-coupon.discount_amount
                self.coupon_repository.update_coupon_status(wallet_obj.wallet_id,code)
                return amount    
        
        raise ValueError("Coupon does not exist")  
              
                   


        
        
