from databasefile.database import DataBase
from models.coupon import Coupon
from models.coupondetails import CouponDetails

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
            
    
    def get_all_coupons(self,wallet_id):
        with self.connection:
            self.cursor.execute(""" 
            SELECT code,discount_amount,minimum_amount,expired_at,is_used
            FROM coupons
            WHERE wallet_id=?
            """,
            (wallet_id,))
            
            coupon_list=[]
            
            row=self.cursor.fetchall()
            if not row:
                return []
            
            for code,discount_amount,minimum_amount,expired_at,is_used in row:
                coupon_list.append(
                    CouponDetails(
                        code=code,
                        discount_amount=discount_amount,
                        minimum_amount=minimum_amount,
                        expired_at=expired_at,
                        is_used=is_used
                    )
                )
        return coupon_list
    
    def update_coupon_status(self,wallet_id,code):
        with self.connection:
            self.cursor.execute(""" 
               UPDATE coupons
               SET is_used=1
               WHERE wallet_id=?
               AND code=?              
            """,
            (wallet_id,code))
       
        