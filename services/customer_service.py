from repositories.customer_repository import CustomerRepository
from models.customer import Customer

class CustomerService:
    def __init__(self,customer_repository):
        self.customer_repository=customer_repository
        
      
    def create_customer(self,first_name,last_name,mobile_number):
        
        customer_obj=Customer(
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number
        )
        
        customer_obj.validate_mobile()

        self.customer_repository.add_customer(customer_obj)
        
        return customer_obj
        