#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import argparse
import urllib
import psycopg2 as psy
import random
import string


####
#define command line input
parser = argparse.ArgumentParser(description='UrlShortener')
parser.add_argument('url', type=str, help='Original URL') 
arguments = parser.parse_args()

####
#check command line input
try:
	urllib.urlopen(arguments.url)
except IOError:
	print "enter URL like 'http(s)://www.example.com' please"
	sys.exit(1)

####
#connect to database
con = None

try:   
	con = psy.connect(database='urlshrtnr', user='postgres', password='postgres')   
	cur = con.cursor()
except psy.DatabaseError, e:
	print 'Error %s' % e    
	sys.exit(1)

####
#make tiny
cur.execute("SELECT tiny FROM shurl")
existing_tiny = cur.fetchall()

#create random string upper, lower and digits
#saverage size of 8 elements
size = 8
tiny = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(size))

#check if tiny already exists otherwise return
if tiny in existing_tiny:
	tiny = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(size))
else:
#make db entry
	try: 
		cur.execute("INSERT INTO shurl (tiny, url) VALUES(%s, %s)", (tiny, arguments.url))
		con.commit()

	except psy.DatabaseError, e:
		if con:
			con.rollback()
			print 'Error %s' % e    
			sys.exit(1)

####
#close db connection
con.close()

#print result
print "your tiny url is: "
print "www.example.com/" + tiny
