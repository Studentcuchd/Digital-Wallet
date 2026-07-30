from databasefile.database import DataBase
from models.customer import Customer

class CustomerRepository:
    def __init__(self,database):
        self.database=database
        self.connection=database.connection
        self.cursor=database.cursor
        
    def add_customer(self,customer):
        with self.connection:
            self.cursor.execute(""" 
            INSERT INTO customers(first_name,last_name,mobile_number)
            VALUES(?,?,?)
            """,
            (customer.first_name,customer.last_name,customer.mobile_number)
            )
            customer.customer_id=self.cursor.lastrowid
            
        