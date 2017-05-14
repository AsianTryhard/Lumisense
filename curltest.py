#!/usr/bin/python

hostname = '192.168.2.6'
username = 'root'
password = 'root'
database = 'angelhack'

import pymysql

conn = pymysql.connect(host = hostname, user = username, passwd = password, db = database)

def getURL(uniqueid):
    cur = conn.cursor()
    cur.execute("SELECT data, active FROM images WHERE uniqueid = " + uniqueid)
    for data, active in cur.fetchall():
        if active == 1:
        	return "false"
        else:
        	cur.execute("UPDATE images SET active = 1 WHERE uniqueid = " + uniqueid)
        	conn.commit()
        	return data

print getURL("778443")