"""
* MySQL Insert *

Insert Into Table -
To fill a table in MySQL, use the "INSERT INTO" statement.
"""
# Insert a record in the "customers" table:
import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "myusername",
  password = "mypassword",
  database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

# Important!: Notice the statement: /mydb.commit()/. It is required to make the changes, otherwise no changes are made to the table.



"""
Insert Multiple Rows -
To insert multiple rows into a table, use the executemany() method.

The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:
"""
import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "myusername",
  password = "mypassword",
  database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
 ('Peter', 'Lowstreet 4'),
 ('Amy', 'Apple st 652'),
 ('Hannah', 'Mountain 21'),
 ('Michael', 'Valley 345'),
 ('Sandy', 'Ocean blvd 2'),
 ('Betty', 'Green Grass 1'),
 ('Richard', 'Sky st 331'),
 ('Susan', 'One way 98'),
 ('Vicky', 'Yellow Garden 2'),
 ('Ben', 'Park Lane 38'),
 ('William', 'Central st 954'),
 ('Chuck', 'Main Road 989'),
 ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record was inserted.")


"""
Get Inserted ID -
You can get the id of the row you just inserted by asking the cursor object.
Note: If you insert more than one row, the id of the last inserted row is returned.
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)