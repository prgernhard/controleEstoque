#! /usr/bin/env pyton
# -*- coding: utf8 -*-

import sqlite3
import os
import sys

# Conectando ao bando de dados database.db
conn = sqlite3.connect("database.db")
cursor  = conn.cursor()


def create_table():
    cursor.execute("drop table Tab_X")
    cursor.execute("CREATE TABLE if not exists Tab_X(A1 TEXT)")
    i = 2
    while i <= 1000:
        locsql = "alter table Tab_X add column A" +  str(i) + " TEXT"  + str(i)
        cursor.execute(locsql)
        i+=1
    print("resgatado da base de dados.: 1")	
def insert_table():



    z = 1
    while z <= 1000:
        x = z
        y = 1001 - z
        locsql1 = "insert into Tab_X (" 
        locsql2 = " values ( "
        i = 1
        while i <= 1000:
            if i > 1:
               locsql2 = locsql2 + ","
               locsql1 = locsql1 + ","
            locsql1 = locsql1 + "A" + str(i)               
            if i == x or i == y :
                locsql2 = locsql2 + "'X'"
            else  :
                locsql2 = locsql2 + "'" "'"

            i+=1
        z +=1     

        #cursor.execute(locsql)
        locsql1 = locsql1 + " ) " + locsql2 + ")"
        cursor.execute(locsql1)

    
def select_table():
    cursor.execute("select * from Tab_X")
    arquivo = open('C:/Temp/teste.txt','w') 
    result = cursor.fetchall()
    for data in result:
         arquivo.write (str(data) +chr(13) )
    arquivo.close



def delete_table():
    cursor.execute("delete from Tab_X")	
	
	
#create_table ()
delete_table ()
insert_table ()
print("resgatado da base de dados.: 2")
select_table ()
print("resgatado da base de dados.: 3")



