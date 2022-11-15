"""
This script tests the PostgreSQL connectivity using Python using `psycopg2`
"""

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Suppliers",
    user="postgres",
    password="admin123")

# TODO: Use best practise to use database.ini instead of above

# Create a cursor
cur = conn.cursor()

# execute a statement
print("PostgreSQL database version: ")
cur.execute("SELECT version()")

# Database server version
db_version = cur.fetchone()
print(db_version)

# Close the communication
cur.close()


