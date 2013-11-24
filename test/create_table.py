#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'blue', 'blue321', 'bluedb');

with con:
   
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Users")
    cur.execute("CREATE TABLE Users(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(30), Device VARCHAR(20), MAC VARCHAR(20), Avail VARCHAR(3))")
    cur.execute("INSERT INTO Users VALUES('','Adam','Windows Phone','40:7A:80:B0:4F:35','NA')")
    cur.execute("INSERT INTO Users VALUES('','Bob','Nexus 7','AC:22:0B:60:39:E2','NA')")
    cur.execute("INSERT INTO Users VALUES('','Carlos','Latptop','C0:18:85:FC:7B:48','NA')")
    cur.execute("INSERT INTO Users VALUES('','Dextor','Playbook','E8:3E:B6:F6:B4:32','NA')")
    cur.execute("INSERT INTO Users VALUES('','Eliot','S3','0C:71:5D:C6:4F:8C','NA')")
