#install Mysql on your computer
#https://dev.mysql.com/downloads/installer/
#pip install mysql 
# pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

#prepare a cursor object 
cursorObject = dataBase.cursor()

#create a database 
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")