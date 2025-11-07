# test_connection.py
# This file's only job is to test the database connection.

from config import DBConfig
from database import MySQLClient
import sys

def check_db_connection():
    print("--- Starting Connection Test ---")
    try:
        # 1. Try to load config
        config = DBConfig()
        print("Config loaded from .env.")

        # 2. Try to create the client (and engine)
        client = MySQLClient(config)
        # If this succeeds, the print statement from the class will appear

    except Exception as e:
        print(f"\n[Error] Failed to create client/engine: {e}")
        sys.exit(1) # Exit with an error code

    try:
        # 3. Try to run a simple, universal query
        # "SELECT 1" is the simplest query to ask a DB "are you alive?"
        print("Attempting to run a test query (SELECT 1)...")
        df = client.query_to_dataframe("SELECT 1")

        if len(df) > 0:
            print("\n[SUCCESS] ✨ Connection is active and query was successful.")
            print("Result of test query:")
            print(df)
        else:
            print("\n[Error] Query ran but returned no data.")

    except Exception as e:
        print(f"\n[Error] Query failed: {e}")
        print("This often means credentials are right, but the database")
        print("name might be wrong or permissions are missing.")

    print("--- Test Finished ---")

if __name__ == "__main__":
    check_db_connection()