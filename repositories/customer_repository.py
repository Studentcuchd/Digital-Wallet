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
            
    
    def get_customer_id_by_number(self,mobile_number):
        self.cursor.execute(""" 
            SELECT customer_id
            FROM customers
            WHERE mobile_number=?
            """,
            (mobile_number,))
        row=self.cursor.fetchone()
        if row is None:
            return None
        
        return row[0]