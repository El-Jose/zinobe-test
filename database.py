import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('test.db')
        print("Connection is established")
    except Error:
        print(Error)

    return con

def create_country_table(con):
    cursorObj = con.cursor()
    try:    
        cursorObj.execute("CREATE TABLE country(region text, name text PRIMARY KEY, language text, time real)")
        con.commit()
    except Error:
        print('Table already exist')

def insert_countries(lst):
    for i in lst:
        try:
            conn.execute('INSERT INTO country VALUES(?, ?, ?, ?)', (i['region'], i['name'], i['language'], i['time']));
            conn.commit()
        except:
            print('Error on insert countries')

conn = sql_connection()
create_country_table(conn)
