import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    database='crud_webservices'
)