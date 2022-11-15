"""
This script describes the best practice to maintain the database credentials
for connectivity with Python and other programs. The idea is to use the 
"database.ini" file maintaining connection variables required. This file should
be mentioned in the .gitignore if the project is to be maintained on GitHub.
"""

import psycopg2
from config import config

def connect():
    """Connect to the PostgreSQL database server
    Returns: TODO

    """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL database
        print("Conencting to the PostgreSQL database..")
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print("PostgreSQL database version: ")
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    connect()
        

