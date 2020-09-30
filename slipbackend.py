import sqlite3

def List():
    conn=sqlite3.connect("list")
    cur=conn.cursor()
    cur.execute("create table if not exists list(id integer primary key,dates text,content text)")
    conn.commit()
    conn.close()
    


def add_list(dates,content):
    conn=sqlite3.connect("list")
    cur=conn.cursor()
    cur.execute("insert into list values(null,?,?)",(dates,content))
    conn.commit()
    conn.close()



def view_list():
    conn=sqlite3.connect("list")
    cur=conn.cursor()
    cur.execute("select * from list")
    row=cur.fetchall()
    conn.close()
    return row



def delete_list(content):
    conn=sqlite3.connect("list")
    cur=conn.cursor()
    cur.execute("delete from list where content=?",(content,))
    conn.commit()
    conn.close()




def update_list(content):
    conn=sqlite3.connect("list")
    cur=conn.cursor()
    cur.execute("update * from list where  content=?",(content,))
    conn.commit()
    conn.close()

List()



  
