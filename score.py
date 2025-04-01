
from mysql.connector import Error

class ScoreManager:
    def __init__(self, db):
        self.connection = db.get_connection()
        self.cursor = db.get_cursor()

    def update_score(self, user_id, score):
        """To update the score for a registered user"""
        try:
            self.cursor.execute("INSERT INTO scores (user_id, score) VALUES (%s, %s)", (user_id, score))
            self.connection.commit()
            print("Votre score a été mis à jour.")
        except Error as error:
            print(f"Votre score n'a pas pu être mis à jour : {error}")

    def get_scores(self):
        """To display scores ordered by descending values"""
        try:
            self.cursor.execute("""
                SELECT users.username, SUM(scores.score) AS total_score
                FROM scores
                JOIN users ON scores.user_id = users.id
                GROUP BY users.username
                ORDER BY total_score DESC""")
            results = self.cursor.fetchall()
            hall_of_fame = {username: total_score for username, total_score in results}
            return hall_of_fame
        except Error as error:
            print(f"Erreur lors de la récupération des scores : {error}")
            return None
    
    def calculate_score(self, result, rows, cols): 
        """To calculate victory of defeat score """
        if rows == 5 and cols == 5:
            return 10 if result == "victory" else -2
        elif rows == 10 and cols == 10:
            return 20 if result == "victory" else -5
        elif rows == 15 and cols == 15:
            return 30 if result == "victory" else -8
        return 0
    
    def get_total_score(self, user_id):
        """To get the total score of a registred"""
        try:
            self.cursor.execute("SELECT SUM(score) FROM scores WHERE user_id = %s", (user_id,))
            result = self.cursor.fetchone()
            return result[0] if result[0] is not None else 0
        except Error as error:
            print(f"Erreur lors de la récupération du score total : {error}")
            return 0