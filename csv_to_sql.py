def csv_to_sql(file,table,con):
    a=csv.reader(file)
    cursor.execute(f'drop table if exists {table}')
    for elem in a:
        if a.line_num==1:
            text="CREATE TABLE IF NOT EXISTS {table}( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,"
            elem=tuple((nom.replace(' ','_') for nom in elem))
            toadd=''.join([nom+" TEXT," for nom in elem])
            text+=toadd[:-1]+");"
            columns=elem
            cols="("+','.join(elem)+")"
            cursor.execute(text)
            con.commit()
        else:
            ho=f"INSERT INTO {table}{cols} VALUES {tuple(elem)};"
            cursor.execute(ho)
    con.commit()
    return columns