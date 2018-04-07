# Python-fun
import MySQLdb
import csv
import sys

class Database:
	host = 'mysql1.cs.clemson.edu'
	user = 'CSAfrmshr_khem'
	password = 'f@rMsh@r3'
	db = 'CSA_farmshare_k8tp'
	
	def __init__ ( self ):
		self.connection = MySQLdb.connect( self.host, self.user, self.password, self.db )
		self.cursor = self.connection.cursor()
		
	def insert( self, query ):
		try:
			self.cursor.execute(query)
			self.connection.commit()
		except:
			self.connection.rollback()
			
	def query ( self, query ):
		cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
		cursor.execute(query)
		#self.connection.commit()
		return cursor.fetchall()
	
	def __del__( self ):
		self.connection.close()		
	
def main(argv):
	db = Database()
	query = """ DELETE FROM Members """
	db.insert(query)

	with open (argv[1]) as csvfile:
		line = csv.reader(csvfile)
		for row in line:
			query = """ INSERT INTO Members (Email) VALUES (' """ + row[0] + """ ') """
			db.insert(query)	

	select = """ SELECT * FROM Members """
	email = db.query(select)
		
	for e in email:
		print ("FOUND %s " % e['Email'])
		
		
if __name__ == "__main__":
	main(sys.argv)		
