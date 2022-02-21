from singleton import Singleton
from pathlib import Path
from db_connector import DbConnection
from eclass.settings import ec_str, Eclass

BASE_DIR = Path(__file__).resolve().parent.parent


class EclassDao(metaclass=Singleton):
	"""
	This class is intended to provide e-class methods
	"""

	def __init__(self, **kwargs) -> None:
		super().__init__()

	# def insert_csv_into_tabel(self, csv, path):
	# 	data = pd.read_csv(path / csv, sep=';')
	# 	df = pd.DataFrame(data)
	# 	for row in df.itertuples():
	#
	# 	print(df)
	# 	return
	#
	# def initialize_db(self):
	# 	csv_data_path = BASE_DIR / 'data/csv'
	# 	onlyfiles = [f for f in listdir(csv_data_path) if isfile(join(csv_data_path, f))]
	# 	""" Initializing CSV files one by one """
	# 	for csv in onlyfiles:
	# 		if csv == 'eClass7_1_CC_en_01_190102xx.csv':
	# 			print(f"Importing csv file {csv}!")
	# 			self.insert_csv_into_tabel(csv, csv_data_path)

	def getFromTable(self, table, filter=''):
		"""
		This method gives data structure according to the given filter
		:param table Is the table name could be None
		:param filter Contains parameters needed for filtering e-class data
		TODO: needs considerations
		"""
		db = DbConnection()
		query = "select * from {}".format(table)
		cursor = db.get_cursor()
		cursor.execute(query)
		rows = cursor.fetchall()
		return rows

	def getClasses(self, filters):
		"""
		This method is to get the e-classes
		:param filters Is the filters given from the front app
		"""
		_type = Eclass.CL
		db = DbConnection()
		query = "select distinct cl.* from {} as cl ".format(ec_str[_type]['table']) + \
				"where (1=1)"
		query = self.setFilters(query, filters, _type, 'cl')
		cursor = db.get_cursor()
		cursor.execute(query)
		rows = cursor.fetchall()
		return rows

	def getProperties(self, cl, filters):
		"""
		This method is to get the properties of cl e-class
		:param cl is the e-class id
		:param filters Is the filters given from the front app
		"""
		_type = Eclass.PR
		db = DbConnection()
		query = "select distinct pr.* from {} as pr ".format(ec_str[Eclass.PR]['table']) + \
				"left join {} as ccpr on pr.IrdiPR = ccpr.IrdiPR ".format(
					ec_str[Eclass.CL]['children'][Eclass.PR]['relation']) + \
				f"where (ccpr.IrdiCC = '{cl}')"
		query = self.setFilters(query, filters, _type, 'pr')

		cursor = db.get_cursor()
		cursor.execute(query)
		rows = cursor.fetchall()
		return rows

	def getValues(self, pr, filters):
		"""
		This method is to get the value items
		:param pr is the property id
		:param filters Is the filters given from the front app
		"""
		_type = Eclass.VA
		db = DbConnection()
		query = "select va.* from {} va ".format(ec_str[Eclass.VA]['table']) + \
				"left join {} prva ".format(ec_str[Eclass.PR]['children'][Eclass.VA]['relation']) + \
				"on va.IrdiVA = prva.IrdiVA " \
				f"where prva.IrdiPR = '{pr}'"
		query = self.setFilters(query, filters, _type, 'va')

		cursor = db.get_cursor()
		cursor.execute(query)
		rows = cursor.fetchall()
		return rows

	def getUnits(self, pr, filters):
		"""
		This method is to get the unit items
		:param pr is the property id
		:param filters Is the filters given from the front app
		"""
		_type = Eclass.UN
		db = DbConnection()
		query = "select un.* from {} un ".format(ec_str[Eclass.UN]['table']) + \
				"left join {} pr ".format(ec_str[Eclass.PR]['children'][Eclass.UN]['relation']) + \
				"on un.IrdiUN = pr.IrdiUN " \
				f"where pr.IrdiPR = '{pr}'"
		query = self.setFilters(query, filters, _type, 'un')

		cursor = db.get_cursor()
		cursor.execute(query)
		rows = cursor.fetchall()
		return rows

	def setFilters(self, query, filters, _type, alias):
		if _type not in filters:
			return query
		q = filters[_type]['q']
		c = filters[_type]['c']
		if q:
			""" If has any search value (q) """
			if c:
				""" If has column (c) then search that column """
				for field in self.getColumnNames(ec_str[_type]['table']):
					if c in field['col']:
						query += " and ({}.{} like '%{}%')".format(alias, c, q)
						break
			else:
				""" If has not any column (c) then search all columns """
				query += " and ("
				for field in self.getColumnNames(ec_str[_type]['table']):
					query += " {}.{} like '%{}%' or".format(alias, field['col'], q)
				""" To remove last extra ' or' """
				query = query[:-3] + ")"

		return query

	def getColumnNames(self, table_name):
		"""
		Returns table name of the given table
		:param table_name Is the desired table name
		"""
		cols = []
		db = DbConnection()
		cursor = db.get_cursor()
		for col in cursor.columns(table=table_name):
			cols.append({
				'col': col.column_name,
				'type': 's',
			})
		return cols
