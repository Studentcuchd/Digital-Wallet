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
    