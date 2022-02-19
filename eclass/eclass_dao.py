from singleton import Singleton
from pathlib import Path
from db_connector import DbConnection
from eclass.settings import ec_str

from .models import createClassDict, createPropertyDict, createValueDict, createUnitDict

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
		db.get_cursor().execute(
			"select * from {}".format(table)
		)
		rows = db.cursor.fetchall()
		return rows

	def getClasses(self):
		"""
		This method is to get the e-classes
		"""
		db = DbConnection()
		query = "select * from {}".format(ec_str['class']['table'])
		db.get_cursor().execute(query)
		rows = db.cursor.fetchall()
		return rows

	def getProperties(self, cl):
		"""
		This method is to get the properties of cl e-class
		:param cl is the e-class id
		"""
		db = DbConnection()
		query = "select * from {} as pr ".format(ec_str['property']['table']) + \
				"inner join {} as ccpr on pr.IrdiPR = ccpr.IrdiPR ".format(
					ec_str['class']['children']['property']['relation']) + \
				f"where ccpr.IrdiCC = '{cl}'"
		db.get_cursor().execute(query)
		rows = db.cursor.fetchall()
		return rows

	def getValues(self, pr):
		"""
		This method is to get the value items
		:param pr is the property id
		"""
		db = DbConnection()
		query = "select va.* from {} va ".format(ec_str['value']['table']) + \
				"left join {} prva ".format(ec_str['property']['children']['value']['relation']) + \
				"on va.IrdiVA = prva.IrdiVA " \
				f"where prva.IrdiPR = '{pr}'"
		db.get_cursor().execute(query)
		rows = db.cursor.fetchall()
		return rows

	def getUnits(self, pr):
		"""
		This method is to get the unit items
		:param pr is the property id
		"""
		db = DbConnection()
		query = "select un.* from {} un ".format(ec_str['unit']['table']) + \
				"left join {} pr ".format(ec_str['property']['children']['unit']['relation']) + \
				"on un.IrdiUN = pr.IrdiUN " \
				f"where pr.IrdiPR = '{pr}'"
		db.get_cursor().execute(query)
		rows = db.cursor.fetchall()
		return rows

	def getDataStructure(self):
		"""
		Creates the data tree from e-class tables
		"""
		structure = {}
		cls = self.getClasses()
		for cl in cls:
			_cl = createClassDict(cl)
			prs = self.getProperties(_cl[ec_str['class']['id']])
			if not prs:
				structure = prepareStructure(structure, _cl, {}, [], [])
				continue
			for pr in prs:
				_pr = createPropertyDict(pr)
				vas = self.getValues(_pr[ec_str['property']['id']])
				_vas = []
				for va in vas:
					_vas.append(createValueDict(va))
				uns = self.getUnits(_pr[ec_str['property']['id']])
				_uns = []
				for un in uns:
					_uns.append(createUnitDict(un))
				structure = prepareStructure(structure, _cl, _pr, _vas, _uns)

		return structure


def prepareStructure(structure, cl, pr, vas, uns):
	"""
	This method adds new items to the structure json object
	:param structure is a json object
	:param cl is the class json
	:param pr is the property json
	:param vas is the value array
	:param uns is the unit array
	"""
	if cl is None:
		return structure

	""" If structure has not the class key, then it is added """
	if cl[ec_str['class']['id']] not in structure:
		structure[cl[ec_str['class']['id']]] = {
			'data': cl,
			'children': {},
		}

	""" If property has no item, then return """
	if ec_str['property']['id'] not in pr:
		return structure

	""" Adding property as the class child """
	structure[cl[ec_str['class']['id']]]['children'][pr[ec_str['property']['id']]] = {
		'data': pr,
		'children': {},
	}

	""" Adding unit as the property child """
	structure[cl[ec_str['class']['id']]]['children'][pr[ec_str['property']['id']]]['children']['unit'] = {
		'data': uns,
	}

	""" Adding value as the property child """
	structure[cl[ec_str['class']['id']]]['children'][pr[ec_str['property']['id']]]['children']['value'] = {
		'data': vas,
	}

	return structure
