from services.transaction_service import TransactionService
from services.coupon_service import CouponService


class TransactionController:
    def __init__(self,transaction_service,coupon_service):
        self.transaction_service=transaction_service
        self.coupon_service=coupon_service
        
    def make_payment(self):
        sender_number=int(input("Sender - enter your 10 digit number="))
        receiver_number=int(input("enter the 10 digit number for payment="))
        amount=int(input("Enter amount="))
        
        coupon_input=input("Do you want to apply coupon yes/no=").lower()
        
        if coupon_input=="yes":
            
            print("Here your available coupons")
            coupon_list=self.coupon_service.show_all_coupons(sender_number)
            
            print("These are your coupons please select one")
            
            for coupon in coupon_list:
                print(
                    f"Code= {coupon.code}, "
                    f"Discount= {coupon.discount_amount}, "
                    f"Minimum Amount={coupon.minimum_amount}, "
                    f"Expiry= {coupon.expired_at}"
                    )
                        
            selected_code=input("Enter the selected code=")
        
            new_amount=self.coupon_service.apply_coupon(sender_number,selected_code,amount)
        
            transaction,cashback=self.transaction_service.make_payment(sender_number,receiver_number,new_amount)
        elif coupon_input=="no":
            transaction,cashback=self.transaction_service.make_payment(sender_number,receiver_number,amount)
        
        else:
            print("Enter yes or no only")
            return  
        
        
        print("Transaction successful")
        print(f"You received a cashback {cashback} rs.")

    
    def transfer_money(self):
        sender_number=int(input("Sender - enter your 10 digit number="))
        receiver_number=int(input("enter the 10 digit number for payment="))
        amount=int(input("Enter amount="))  
        transaction=self.transaction_service.transfer_money(sender_number,receiver_number,amount)

        print("Transaction successful")
        
    def get_summary(self):
        number=int(input("enter your 10 digit number="))
        summary=self.transaction_service.get_spending_summary(number)
        print(f"Total Transactions = {summary.total_transactions}")
        print(f"Total Money Spent = {summary.total_money_spend}")
        print(f"Total Money Received = {summary.total_money_get}")
    
    
    def get_transaction_history(self):
        mobile_number = int(input("Enter your 10 digit number = "))

        history_list = self.transaction_service.get_transaction_history(mobile_number)

        print(" Transaction History ")

        for history in history_list:
            print(
                f"Amount = {history.amount}, "
                f"Type = {history.transaction_type}, "
                f"Status = {history.status}, "
                f"Date = {history.created_at}"
            )    

