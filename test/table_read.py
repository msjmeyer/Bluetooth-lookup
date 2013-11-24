#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'blue', 'blue321', 'bluedb');

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM Users")

    rows = cur.fetchall()

    for row in rows:
        print row
