#! /usr/bin/python

import sqlite3

conn = sqlite3.connect('prueba.db')
print ('openned database success')

conn.execute(
"""
    insert into company (id, name, age, address, salary)
    values (1,"miguel", 22, "bogota", 2000000);    
"""
)

conn.execute(
"""
    insert into company (id, name, age, address, salary)
    values (2,"jonny", 22, "bogota", 2500000);    
"""
)

conn.execute(
"""
    insert into company (id, name, age, address, salary)
    values (3,"Maribel", 27, "Cali", 1500000);   
"""
)

conn.execute(
"""
   insert into company (id, name, age, address, salary)
    values (4,"Laura", 21, "Cali", 6000000);
"""
)
    
 

conn.commit()
print ("record created successfully")
conn.close()

