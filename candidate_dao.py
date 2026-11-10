from db_connection import get_connection

def get_all_candidates():
    """
    Function to fetch all candidates from the database.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True) # dictionary=True se data column names ke sath milta hai

        cursor.execute("SELECT * FROM candidate;")
        candidates = cursor.fetchall()

        cursor.close()
        conn.close()
        return candidates
    except Exception as e:
        print(f"❌ Error while fetching candidates: {e}")
        return []