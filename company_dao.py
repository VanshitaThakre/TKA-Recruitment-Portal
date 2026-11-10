from db_connection import get_connection

def get_all_companies():
    """
    Function to fetch all companies from the database.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM company;")
        companies = cursor.fetchall()
        
        cursor.close()
        conn.close()
        return companies
    except Exception as e:
        print(f"❌ Error while fetching companies: {e}")
        return []