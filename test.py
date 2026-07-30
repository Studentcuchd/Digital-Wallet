def validate_mobile(num):
    if len(str(num)) != 10:
        raise f"Mobile number is not valid"
    
    else:
        print("number validate")
        

num=1234567890
validate_mobile(num)