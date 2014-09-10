#coding=utf-8

import sqlite3

cx=sqlite3.connect("test.db")
cu=cx.cursor()
#cu.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")

#for t in[(0,10,'abc','Yu'),(1,20,'cba','Xu')]:
#    cx.execute("insert into catalog values (?,?,?,?)", t)
#cx.commit()   

x=u'张'
cu.execute("update catalog set name=? where id=0",x)

cu.execute("select * from catalog")
for item in cu.fetchall():
    for element in item:
        print element,  
    print

