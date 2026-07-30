class Customer:
    def __init__(self,first_name,last_name,mobile_number,customer_id=None):
        self.first_name=first_name
        self.last_name=last_name
        self.mobile_number=mobile_number
        self.customer_id=customer_id

    def validate_mobile(self):
        number=str(self.mobile_number)
        
        if not number.isdigit():
            raise TypeError("Only digits are accepted please chekc your number once")
               
        elif len(number) !=10:
            raise ValueError("Your mobile number is not having 10 digits please carefully check it")
        
        elif number[0] not in "6789":
            raise ValueError("Invalid mobile number pleaser enter mobile number correctly its a fake number")
        
        else:
            return True