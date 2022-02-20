import pyodbc
from dundts_backend import settings
from singleton import Singleton


class DbConnection(metaclass=Singleton):
	"""
	Is the singleton class for creating and maintaining database connection
	"""
	def __init__(self):
		driver = 'SQLITE3'
		server = 'localhost'
		database = settings.DATABASES['default']['NAME']
		print('Connecting to the database: ', database, '...')
		self.dbconn = pyodbc.connect("DRIVER={};".format(driver) + \
									 "SERVER={};".format(server) + \
									 "DATABASE={};".format(database) + \
									 'Trusted_Connection=yes;' + \
									 "CHARSET=UTF8",
									 ansi=True)

	def get_cursor(self):
		return self.dbconn.cursor()

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.dbconn.close()
