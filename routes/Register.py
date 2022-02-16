from flask import request
from ... import Database

mydb=Database.mydb

def main():
    if request.method == "POST":
        mycursor = mydb.cursor()
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        return {"message": "eyyo"}
    else:
        mycursor = mydb.cursor()
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        return {"error": "nop"}