import psycopg2
def createTable():
    db = psycopg2.connect("dbname='db' user='postgres' host='localhost' password='abdu123' port='5432'")

    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT,quantity INTIGER,price REAL)")
    cur.execute("INSERT INTO store VALUES('book',10,15.50)")
    db.commit()
    db.close()

# def insert(item,qty,price):
#     db = psycopg2.connect("dbname='db' user='postgres' host='localhost' password='abdu123' port='5432'")
#     cur = db.cursor()
#     cur.execute("INSERT INTO store VALUES(?,?,?)",(item,qty,price))
#     db.commit()
#     db.close()

# def view():
#     db = psycopg2.connect("dbname='db' user='postgres' host='localhost' password='abdu123' port='5432'")
#     cur = db.cursor()
#     cur.execute('SELECT * FROM store')
#     rows = cur.fetchall()
#     db.close()
#     return rows
# def delete(item):
#     db = psycopg2.connect("dbname='db' user='postgres' host='localhost' password='abdu123' port='5432'")
#     cur = db.cursor()
#     cur.execute("DELETE FROM store WHERE item=?",(item,))
#     db.commit()
#     db.close()
# def update(item,qty,price):
#     db = psycopg2.connect("dbname='db' user='postgres' host='localhost' password='abdu123' port='5432'")
#     cur = db.cursor()
#     cur.execute("UPDATE store SET quantity=?,price=?  WHERE item=?",(qty,price,item))
#     db.commit()
#     db.close()




# print(view())