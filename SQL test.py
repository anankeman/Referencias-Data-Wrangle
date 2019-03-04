# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 22:20:57 2018

@author: Pippo
"""
#import pyodbc
import mysql.connector as mariadb
#import MySQLdb
mariadb_connection = mariadb.connect(user='root', password='00mayaman', database='hausapp')
c = mariadb_connection.cursor()

c.execute("DESCRIBE gumtree;")

rows = c.fetchall()

for eachRow in rows:
    print(eachRow)