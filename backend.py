import sqlite3

#create table in database
def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY,title text,author text, year integer, isbn integer) ")
    conn.commit()
    conn.close()

#insert
def insert(title,author,year,isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

#view
def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows = cur.fetchall()
    conn.close()
    return rows

#search
def search(title="",author="",year="",isbn=""): #create empty strings to solve error when we receive only one value
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

#delete
def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM bookstore WHERE id=?",(id,))
    conn.commit()
    conn.close()

#update
def update(id,title,author,year,isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
