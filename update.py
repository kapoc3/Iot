#! /usr/bin/python

import sqlite3

conn = sqlite3.connect('prueba.db')
print ('openned database success')

cursor = conn.execute(
"""
    update company set salary = 2500 where id = 1
"""
)
conn.commit()

cursor = conn.execute(
"""
    select id, name, address, salary from company
"""
)

for row in cursor:
    print ("id= ", row[0])
    print ("name= ", row[1])
    print ("address= ", row[2])
    print ("salary= ", row[3])
    
print ("operation was success")

conn.close()