from db_connection import get_connection

class ApplicationDao:
    @staticmethod
    def get_all_applications():
        connection = get_connection()  # yahan bhi get_connection hoga
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM application")
        applications = cursor.fetchall()
        cursor.close()
        connection.close()
        return applications