"""
*MySQL Create Database* 

Creating a Database -
To create a database in MySQL, use the "CREATE DATABASE" statement:
"""
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "my_user_name",
    password = "my_password"
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE my_data_base")



"""
Check if Database Exists -
You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:
"""
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "my_user_name",
    password = "my_password"
)

my_cursor = mydb.cursor()

my_cursor.execute("SHOW DATABASES")

for x in my_cursor:
    print(x)
    
""" Or you can try to access the database when making the connection: """
import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "myusername",
  password = "mypassword",
  database = "mydatabase"
)

# If this page is executed with no error, the database "mydatabase" exists in your system
# If the database does not exist, you will get an error.