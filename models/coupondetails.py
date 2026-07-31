class CouponDetails:
    def __init__(self,code,discount_amount,minimum_amount,expired_at,is_used):
        self.code=code
        self.discount_amount=discount_amount
        self.minimum_amount=minimum_amount
        self.expired_at=expired_at
        self.is_used=is_used