import sqlite3
import tkinter as tk
from tkinter import ttk
import csv

con=sqlite3.connect("temp.db")
cursor=con.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS
users(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    age INTEGER
);""");


con.commit()
for elem in [("olivier",30),("bertrand",50)]:
    cursor.execute(f"INSERT INTO users(name,age) VALUES {elem};")
cursor.execute("SELECT * FROM users")

def execute():
    sqlite3.PARSE_COLNAMES=True
    cursor.execute(e.get("1.0","end"))
    con.commit()
    tablo.delete(*tablo.get_children())
    titres=[kaka[0] for kaka in cursor.description]
    tablo.config(columns=titres)
    for titre in titres:
        tablo.column(titre,width=100)
        tablo.heading(titre,text=titre)
    tablo["show"]="headings"
    for elem in cursor:
        tablo.insert(parent='',index=0,values=elem)
    tablo.pack()
    con.rollback()

f=tk.Tk()
f.title("SQLite3 Viewer")
f.geometry("800x600")
f.resizable(False,False)

e=tk.Text(f)
e.insert("1.0","select * from users;")
e.pack()

b=tk.Button(f,command=execute,text="execute")
b.pack()

tablo=ttk.Treeview(f)
tablo.pack()

f.mainloop()
