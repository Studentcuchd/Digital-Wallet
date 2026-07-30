from databasefile.database import DataBase
from models.transaction import Transaction

class TransactionRepository:
    def __init__(self,database):
        self.database=database
        self.connection=database.connection
        self.cursor=database.cursor
        
    def add_transaction(self,transaction):
        with self.connection:
            self.cursor.execute(""" 
            INSERT INTO transactions(sender_wallet_id,receiver_wallet_id,amount,transaction_type,status,created_at)
            VALUES(?,?,?,?,?,?)
            """,
            (transaction.sender_wallet_id,transaction.receiver_wallet_id,transaction.amount,transaction.transaction_type,transaction.status,transaction.created_at)
            )
            transaction.transaction_id=self.cursor.lastrowid
            
            