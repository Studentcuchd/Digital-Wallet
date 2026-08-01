from services.customer_service import CustomerService

class CustomerController:
    def __init__(self,customer_service):   
        self.customer_service=customer_service

        
    def create_customer(self):
        first_name=input("Enter your first name=")
        last_name=input("Enter your last name=")
        mobile_number=int(input("Enter your 10 digit number="))
        
        customer=self.customer_service.create_customer(first_name,last_name,mobile_number)
        
        print("Customer added successfully")
        print(f"First Name={customer.first_name} Last Name={customer.last_name}  Mobile Number={customer.mobile_number}")
        