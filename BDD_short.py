import sqlite3
import tkinter as tk
from tkinter import ttk
from csv_to_sql import csv_to_sql

con=sqlite3.connect("ipt.sqlite3")
cursor=con.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS
users(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    age INTEGER
);""");
with open("keywords.list","r") as f:
    keywords=f.read().split("\n")


def check():
    e.tag_remove('found', '1.0', tk.END)
    for word in keywords:
        idx = '1.0'
        while idx:
            idx = e.search(word, idx, nocase=1, stopindex=tk.END)
            if idx:
                lastidx = '%s+%dc' % (idx, len(word))
                e.tag_add('found', idx, lastidx)
                idx = lastidx
    e.tag_config('found', foreground='red')
con.commit()
for elem in [("olivier",30),("bertrand",50)]:
    cursor.execute(f"INSERT INTO users(name,age) VALUES {elem};")
cursor.execute("SELECT * FROM users")

def execute():
    check()
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
f.configure(background="#8b0000")
f.geometry("800x600")
f.resizable(False,False)

# csv_to_sql(open("tr.csv","r"),'users',con,cursor)

e=tk.Text(f,background="#6c1413",foreground="white",font=("Consolas",12))
e.insert("1.0","select * from users;")
e.pack()
check()
b=tk.Button(f,command=execute,text="execute")
b.pack()
f.style=ttk.Style()

f.style.configure('TreeView', background = 'red', foreground = 'white', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
f.attributes("-fullscreen", True)
tablo=ttk.Treeview(f)
tablo.pack()
b=tk.Button(f,command=f.quit,text="tchao")
b.pack()
f.bind('<Control-s>',lambda event:con.commit())
f.bind('<Control-r>',lambda event:con.rollback())
f.bind('<KeyRelease>',lambda event:check())
f.mainloop()
