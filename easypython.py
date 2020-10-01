# -*- coding: UTF-8 -*-
import MySQLdb                # here we import Mysqlbd 
import sys                    # we import sys

reload(sys)
sys.setdefaultencoding('utf-8')

db = MySQLdb.connect(user='root', db='myblog', passwd='jacky983', host='114.215.154.9',charset='utf8')
cursor = db.cursor()
cursor.execute('SELECT blogtitle FROM blogs')
for row in cursor.fetchall():
    str=row[0] 
    print str
db.close()

