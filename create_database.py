import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()
passw = os.getenv("PASSWORD")

class CreateDatabase:
    def __init__(self):
        self.connection = self.create_connection()
        self.create_database()
        self.create_user_table()
        self.create_score_table()
    
    