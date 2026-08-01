from databasefile.database import DataBase
from models.transaction import Transaction
from models.history import History
from models.spending_summary import SpendingSummary

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
    
    def get_spend_summary(self,wallet_id):
        with self.connection:
            self.cursor.execute(""" 
                SELECT COUNT(*) from transactions 
                WHERE sender_wallet_id=?
                OR receiver_wallet_id=?
                """,
                (wallet_id,wallet_id))
            
            row1=self.cursor.fetchone()
            total_transactions=row1[0]
        
            self.cursor.execute(""" 
                SELECT SUM(amount) 
                FROM transactions
                WHERE sender_wallet_id=?
                """,
                (wallet_id,))
            row2=self.cursor.fetchone()
            spend_amount=row2[0]
            if spend_amount is None:
                spend_amount=0

            self.cursor.execute(""" 
                SELECT SUM(amount) 
                FROM transactions
                WHERE receiver_wallet_id=?
                """,
                (wallet_id,))
            row3=self.cursor.fetchone()
            received_amount=row3[0]            
            if received_amount is None:
                received_amount=0
    
        return SpendingSummary(
        total_money_spend=spend_amount,
        total_money_get=received_amount,
        total_transactions=total_transactions
        )