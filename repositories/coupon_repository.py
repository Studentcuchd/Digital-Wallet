from databasefile.database import DataBase
from models.coupon import Coupon

class CouponRepository:
    def __init__(self,database):
        self.database=database
        self.connection=database.connection
        self.cursor=database.cursor
        
    def add_coupon(self,coupon):
        with self.connection:
            self.cursor.execute(""" 
            INSERT INTO coupons(wallet_id,code,discount_amount,minimum_amount,expired_at,is_used)
            VALUES(?,?,?,?,?,?)
            """,
            (coupon.wallet_id,coupon.code,coupon.discount_amount,coupon.minimum_amount,coupon.expired_at,coupon.is_used)
            )
            coupon.coupon_id=self.cursor.lastrowid
            
            