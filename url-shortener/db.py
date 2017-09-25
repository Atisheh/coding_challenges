#!/usr/bin/python
# -*- coding: utf-8 -*-
from psycopg2 import connect
import sys


#class UrlList(object):
def main():
	con = None

	#def __init__(self):
	try:   
		con = connect(database='urlshrtnr', user='postgres', password='postgres')   
		cur = con.cursor()
	except DatabaseError, e:
		print 'Error %s' % e    
		sys.exit(1)

	#def insertEntry(self, url, tiny):
	try: 
		cur.execute("INSERT INTO shurl VALUES(url, tiny)")
		con.commit()

	except DatabaseError, e:
		if con:
			con.rollback()
			print 'Error %s' % e    
			sys.exit(1)

	#def getTiny(self):

	cur.execute("SELECT tiny FROM shurl")
	#return cur.fetchall()
	print cur.fetchall()

	#def closeDB(self):
	con.close()


if __name__ == '__main__':
	main()
	#pass
	# for e in sl.getTiny():
	# 	print e
