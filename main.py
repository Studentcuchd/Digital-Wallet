from databasefile.database import DataBase


from repositories.customer_repository import CustomerRepository
from repositories.wallet_repository import WalletRepository
from repositories.transaction_repository import TransactionRepository
from repositories.coupon_repository import CouponRepository


from services.customer_service import CustomerService
from services.wallet_service import WalletService
from services.transaction_service import TransactionService
from services.coupon_service import CouponService



from controller.customer_controller import CustomerController
from controller.wallet_controller import WalletController
from controller.transaction_controller import TransactionController


def main():

    database = DataBase("DigitalWallet.db")


    customer_repository = CustomerRepository(database)
    wallet_repository = WalletRepository(database)
    transaction_repository = TransactionRepository(database)
    coupon_repository = CouponRepository(database)



    coupon_service = CouponService(coupon_repository,wallet_repository)

    customer_service = CustomerService(customer_repository)

    wallet_service = WalletService(wallet_repository,customer_repository,coupon_service)

    transaction_service = TransactionService(transaction_repository,wallet_repository)



    customer_controller = CustomerController(customer_service)

    wallet_controller = WalletController(wallet_service)

    transaction_controller = TransactionController(transaction_service,coupon_service)



    while True:
        try:
            print("\n MAIN MENU DIGITALWALLET")
            print("1. Register Customer")
            print("2. Create Wallet")
            print("3. Add Money")
            print("4. Check Balance")
            print("5. Transfer Money")
            print("6. Make Payment")
            print("7. Spending Summary")
            print("8. Transaction History")
            print("9. Exit")

            choice = int(input("Enter your choice= "))

            if choice == 1:
                customer_controller.create_customer()

            elif choice == 2:
                wallet_controller.create_wallet()

            elif choice == 3:
                wallet_controller.add_money()

            elif choice == 4:
                wallet_controller.get_balance()

            elif choice == 5:
                transaction_controller.transfer_money()

            elif choice == 6:
                transaction_controller.make_payment()

            elif choice == 7:
                transaction_controller.get_summary()

            elif choice == 8:
                transaction_controller.get_transaction_history()

            elif choice == 9:            
                break

            else:
                print("enter valid choice")
            
            
        except Exception as e:
            print(f"Error= {e}")

main()