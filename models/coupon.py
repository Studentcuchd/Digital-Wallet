class Coupon:
    def __init__(self,wallet_id,code,discount_amount,minimum_amount,expired_at,is_used=False,coupon_id=None):
        self.wallet_id=wallet_id
        self.code=code
        self.discount_amount=discount_amount
        self.minimum_amount=minimum_amount
        self.expired_at=expired_at
        self.is_used=is_used
        self.coupon_id=coupon_id 

                                              