import pyodbc
from dundts_backend import settings
from singleton import Singleton


class DbConnection(metaclass=Singleton):
	"""
	Is the singleton class for creating and maintaining database connection
	"""
	def __init__(self):
		self.driver = 'SQLITE3'
		self.server = 'localhost'
		self.database = settings.DATABASES['default']['NAME']
		print('Connecting to the database: ', self.database, '...')
		self.dbconn = pyodbc.connect("DRIVER={};".format(self.driver) + \
									 "SERVER={};".format(self.server) + \
									 "DATABASE={};".format(self.database) + \
									 'Trusted_Connection=yes;' + \
									 "CHARSET=UTF8",
									 ansi=True)
		self.cursor = self.dbconn.cursor()

	def get_cursor(self):
		return self.cursor

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.dbconn.close()
