import sqlite3
import tkinter as tk
from tkinter import ttk
import csv
con=sqlite3.connect("ma_base.db")
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
    cursor.execute(e.get("1.0","end"))
    con.commit()
    tablo.delete(*tablo.get_children())
    tablo.get
    titres=[kaka[0] for kaka in cursor.description]
    tablo.column("#0")
    for titre in titres:
        tablo.column(titre,width=100)
        tablo.heading(titre,text=titre)
    tablo["show"]="headings"
    for elem in cursor:
        tablo.insert(parent='',index='end',iid=0,text='',values=elem)
    tablo.pack()
    con.rollback()
f=tk.Tk()
style = ttk.Style()
style.theme_use('clam')
e=tk.Text(f)
e.pack()

b=tk.Button(f,command=execute,text="execute")
b.pack()

a=csv.reader(open("BDD_short.csv","r"))
cursor.execute('drop table if exists underscore')
for elem in a:
    if a.line_num==1:
        text="CREATE TABLE IF NOT EXISTS underscore( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,"
        elem=tuple((nom.replace(' ','_') for nom in elem))
        toadd=''.join([nom+" TEXT," for nom in elem])
        text+=toadd[:-1]+");"
        cadre=tk.Frame(f)
        cadre.pack()
        tablo=ttk.Treeview(cadre)
        tablo["columns"]=elem
        
        cols="("+','.join(elem)+")"
        cursor.execute(text)

        con.commit()
    else:
        ho=f"INSERT INTO underscore{cols} VALUES {tuple(elem)};"
        cursor.execute(ho)
con.commit()
        

