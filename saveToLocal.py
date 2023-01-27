import sqlite3
import uuid

conn = sqlite3.connect('local.db')
c = conn.cursor()


# bikin table respon
# c.execute('''CREATE TABLE respon
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#               status varchar(20) NOT NULL,
#               data text(200) NOT NULL)''')
#
# c.execute('''CREATE TABLE invoice
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#               number varchar(100) NOT NULL,
#               data text(200) NOT NULL)''')

# c.execute('''CREATE TABLE err_inv
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#               number varchar(100) NOT NULL,
#               data text(200) NOT NULL)''')
def create_respon(data):
    c.execute("INSERT INTO respon (status,data) VALUES ('" + data[0] + "','" + data[1] + "')")
    conn.commit()


def create_error(inv, message):
    c.execute("INSERT INTO err_inv (number,data) VALUES ('" + inv + "','" + message + "')")
    conn.commit()


def create_data_inv(inv, data):
    c.execute("INSERT INTO invoice (number,data) VALUES ('" + inv + "','" + data + "')")
    conn.commit()
