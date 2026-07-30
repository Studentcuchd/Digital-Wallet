import sqlite3

class DataBase:
    def __init__(self,db_name):
        self.connection=sqlite3.connect(db_name)
        self.cursor=self.connection.cursor()
        
        self.create_table()
        
    def create_table(self):
        with self.connection:
            
            self.cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS customers(
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                mobile_number INTEGER NOT NULL UNIQUE 
                );
                """)
            
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS wallets(
                wallet_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL UNIQUE,
                balance INTEGER DEFAULT 0,
                 
                FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
                );
                """)
            
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS coupons(
                coupon_id INTEGER PRIMARY KEY AUTOINCREMENT,
                wallet_id INTEGER NOT NULL,
                code TEXT NOT NULL,
                discount_amount INTEGER NOT NULL DEFAULT 0,
                minimum_amount INTEGER NOT NULL,
                expired_at DATE NOT NULL,
                is_used INTEGER DEFAULT 0,
                
                FOREIGN KEY(wallet_id) REFERENCES wallets(wallet_id)
                );
                """)
            
            self.cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS transactions(
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender_wallet_id INTEGER NOT NULL,
                receiver_wallet_id INTEGER NOT NULL,
                amount INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at DATE NOT NULL,

                FOREIGN KEY(sender_wallet_id) REFERENCES wallets(wallet_id),
                FOREIGN KEY(receiver_wallet_id) REFERENCES wallets(wallet_id)
                
                );
                
                """)
    
    def commit(self):
        self.connection.commit()
        
    def rollback(self):
        self.connection.rollback()
        
    def close(self):
        self.connection.close()  