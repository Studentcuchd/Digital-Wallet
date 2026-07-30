import datetime
class Coupon:
    def __init__(self,wallet_id,code,discount_amount,minimum_amount,expired_at,is_used=False,coupon_id=None):
        self.wallet_id=wallet_id
        self.code=code
        self.discount_amount=discount_amount
        self.minimum_amount=minimum_amount
        self.expired_at=expired_at
        self.is_used=is_used
        self.coupon_id=coupon_id 


    def validate_coupon_expiry(self):
        if self.expired_at<datetime.date.today():
            raise ValueError("Your coupon has expired")    
        
        elif self.is_used:
            raise ValueError("Your coupon is already used") 
        
        else:
            return True
        
        
    def mark_coupon_use(self):
        self.is_used=True
        
    def coupon_applicable(self,amount):
        if amount>=self.minimum_amount:
            return True
        else:
            raise ValueError("Your coupon is not eligible for this as your amount is less than minimum amount")
        
        
        
    