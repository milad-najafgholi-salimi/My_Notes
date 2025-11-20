"""
MySQL Get Started -

1) Download MySQL from MySQL.com
2) Install MySQL Driver (Here we will use "MySQL Connector"):
    * Python needs a MySQL driver to access the MySQL database.
    * Recommend to use PIP to install "MySQL Connector".
    * Navigate your command line to the location of PIP, and type the following:
        Download and install "MySQL Connector":
            "C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector-python"

What the MySQL Connector actually does:
mysql-connector-python only adds one capability:
It lets your Python code connect to a MySQL database and run SQL queries.
Which means you can't run SQL code in Python module directly. So you need connector.
"""

# Run the following code and if you didn't get any errors, it works well:
import mysql.connector


# Create Connection
# Use the username and password from your MySQL database:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword"
)

print(mydb)




# Point: With this driver, you can work with python in VsCode.

