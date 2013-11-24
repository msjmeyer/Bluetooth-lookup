#!/usr/bin/python
import MySQLdb as mdb
import bluetooth
import time

con = mdb.connect('localhost', 'blue', 'blue321', 'bluedb')

while True:
    cur = con.cursor()
    result = bluetooth.lookup_name('E8:3E:B6:F6:B4:32', timeout=5)
    if (result != None): cur.execute("UPDATE Users SET Avail=%s WHERE MAC=%s",('yes','E8:3E:B6:F6:B4:32'))
    else: cur.execute("UPDATE Users SET Avail=%s WHERE MAC=%s",('no','E8:3E:B6:F6:B4:32'))

    result = bluetooth.lookup_name('AC:22:0B:60:39:E2', timeout=5)
    if (result != None): cur.execute("UPDATE Users SET Avail=%s WHERE MAC=%s",('yes','AC:22:0B:60:39:E2'))
    else: cur.execute("UPDATE Users SET Avail=%s WHERE MAC=%s",('no','AC:22:0B:60:39:E2'))

    result = bluetooth.lookup_name('40:7A:80:B0:4F:35', timeout=5)
    if (result != None): cur.execute("UPDATE Users SET Avail=%s WHERE MAC=%s",('yes','40:7A:80:B0:4F:35'))
    else: cur.execute("UPDATE Users SET Avail=%s WHERE MAC=%s",('no','40:7A:80:B0:4F:35'))

    result = bluetooth.lookup_name('C0:18:85:FC:7B:48', timeout=5)
    if (result != None): cur.execute("UPDATE Users SET Avail=%s WHERE MAC=%s",('yes','C0:18:85:FC:7B:48'))
    else: cur.execute("UPDATE Users SET Avail=%s WHERE MAC=%s",('no','C0:18:85:FC:7B:48'))    

    result = bluetooth.lookup_name('0C:71:5D:C6:4F:8C', timeout=5)
    if (result != None): cur.execute("UPDATE Users SET Avail=%s WHERE MAC=%s",('yes','0C:71:5D:C6:4F:8C'))
    else: cur.execute("UPDATE Users SET Avail=%s WHERE MAC=%s",('no','0C:71:5D:C6:4F:8C'))




    con.commit()
    time.sleep(300)

