#-*- encoding: utf-8 -*-
import urllib
import db


class Shortener(object):

	#Konstruktor
	def __init__(self, url):	
		self.url = url	

# setter
	def setURL(self, url):
		self.url = url

# getter   
	def getURL(self):
		return self.url

#functions
	def shortenIt(self):

		#get existing tiny's to check uniqueness
		existing_tiny[] = self.con.getTiny()

		#create random string upper, lower and digits
		#saverage size of 8 elements
		size = 8
		tiny = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(size))
		
		#check if tiny already exists otherwise return
		if tiny in existing_tiny 
			tiny = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(size))
		else
			#merge www with tiny and return
			return "www.example.com/" + tiny

	def entryDB(self):
		#make db entry
		self.con.insertEntry(self.link, self.filename, self.bitrate, self.format)

if __name__ == '__main__':
	pass

	# recordOne = Record('http://www.fluxfm.de/stream-berlin', 10, 'test', 128)
	# recordOne.recordStream()
	# recordOne.useDB()
	# recordOne.showRecords()

	#TAGS RAUS!
