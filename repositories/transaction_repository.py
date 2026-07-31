from databasefile.database import DataBase
from models.transaction import Transaction
from models.history import History

class TransactionRepository:
    def __init__(self,database):
        self.database=database
        self.connection=database.connection
        self.cursor=database.cursor
        
    def add_transaction(self,transaction):

        self.cursor.execute(""" 
        INSERT INTO transactions(sender_wallet_id,receiver_wallet_id,amount,transaction_type,status,created_at)
        VALUES(?,?,?,?,?,?)
        """,
        (transaction.sender_wallet_id,transaction.receiver_wallet_id,transaction.amount,transaction.transaction_type,transaction.status,transaction.created_at)
        )
        transaction.transaction_id=self.cursor.lastrowid
        
    
    def get_all_transaction(self,wallet_id):
        with self.connection:
            self.cursor.execute("""
            SELECT amount,transaction_type,status,created_at
            FROM transactions
            WHERE sender_wallet_id=?
            OR receiver_wallet_id=?
            """,
            (wallet_id,wallet_id))
            
            row=self.cursor.fetchall()
            history_list=[]
            for amount,transaction_type,status,created_at in row:
                history_obj=History(
                    amount=amount,
                    transaction_type=transaction_type,
                    status=status,
                    created_at=created_at 
                )
                history_list.append(history_obj)
        
        return history_list