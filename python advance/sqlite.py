import sqlite3

def createTable():
    conn=sqlite3.connect("dummy.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(name,quantity,price):
    conn=sqlite3.connect("dummy.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO store VALUES (?,?,?)",(name,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("dummy.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows=cursor.fetchall()
    conn.close()
    return rows
    
def delete(name):
    conn=sqlite3.connect("dummy.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM store WHERE item = (?)",[name])
    conn.commit()
    conn.close()
    
def update(name,quantity,price):
    conn=sqlite3.connect("dummy.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item = ?",(quantity,price,name))
    conn.commit()
    conn.close()

createTable()
insert("Beer",20,200)
# delete("Beer") 
# update('Beer',30,400)
print([i for i in view()])
