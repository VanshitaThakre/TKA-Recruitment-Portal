from db_connection import get_connection

class JobDao:
    @staticmethod
    def get_all_jobs():
        connection = get_connection()  # yahan get_db_connection ki jagah get_connection hoga
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM job")
        jobs = cursor.fetchall()
        cursor.close()
        connection.close()
        return jobs