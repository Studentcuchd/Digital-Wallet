from databasefile.database import DataBase
from models.wallet import Wallet

class WalletRepository:
    def __init__(self,database):
        self.database=database
        self.connection=database.connection
        self.cursor=database.cursor
        
    def create_wallet(self,wallet):
        with self.connection:
            self.cursor.execute(""" 
            INSERT INTO wallets(customer_id,balance)
            VALUES (?,?)
            """,
            (wallet.customer_id,wallet.balance)
            )
            wallet.wallet_id=self.cursor.lastrowid
    

    
    def get_wallet_by_number(self,number):
        with self.connection:
            self.cursor.execute("""
            SELECT wallets.wallet_id,wallets.customer_id,wallets.balance
            FROM wallets
            JOIN customers
            ON wallets.customer_id=customers.customer_id
            WHERE customers.mobile_number=?
            """,
            (number,))
            
        row=self.cursor.fetchone()
        
        if row is None:
            return None
        
        return Wallet(
            wallet_id=row[0],
            customer_id=row[1],
            balance=row[2]
        )
        
        
        
    def update_balance(self,wallet_id,balance):
        self.cursor.execute("""
        UPDATE wallets
        SET balance=?
        WHERE wallet_id=?
        """,
        (balance,wallet_id))
        
    def get_balance(self,wallet_id):
        self.cursor.execute(""" 
        SELECT balance 
        FROM wallets
        WHERE wallet_id=?
        """,
        (wallet_id,))
        
        row=self.cursor.fetchone()
        balance=row[0]
        return balance
    