from singleton import Singleton
from pathlib import Path
from db_connector import DbConnection
from eclass.settings import ec_str

import eclass.models as mdl

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
		_type = 'class'
		db = DbConnection()
		query = "select distinct cl.* from {} as cl ".format(ec_str[_type]['table']) + \
				"where (1=1)"
		# filters['class'] = {
		# 	'v': True,
		# 	'q': "AEI",
		# }
		query = setFilters(query, filters, _type, 'cl')
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
		_type = 'property'
		db = DbConnection()
		query = "select distinct pr.* from {} as pr ".format(ec_str['property']['table']) + \
				"left join {} as ccpr on pr.IrdiPR = ccpr.IrdiPR ".format(
					ec_str['class']['children']['property']['relation']) + \
				f"where (ccpr.IrdiCC = '{cl}')"
		filters[_type] = {
			'v': True,
			'q': "Manufacturer",
		}
		query = setFilters(query, filters, _type, 'pr')

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
		_type = 'value'
		db = DbConnection()
		query = "select va.* from {} va ".format(ec_str['value']['table']) + \
				"left join {} prva ".format(ec_str['property']['children']['value']['relation']) + \
				"on va.IrdiVA = prva.IrdiVA " \
				f"where prva.IrdiPR = '{pr}'"
		query = setFilters(query, filters, _type, 'va')

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
		_type = 'unit'
		db = DbConnection()
		query = "select un.* from {} un ".format(ec_str['unit']['table']) + \
				"left join {} pr ".format(ec_str['property']['children']['unit']['relation']) + \
				"on un.IrdiUN = pr.IrdiUN " \
				f"where pr.IrdiPR = '{pr}'"
		query = setFilters(query, filters, _type, 'un')

		cursor = db.get_cursor()
		cursor.execute(query)
		rows = cursor.fetchall()
		return rows

	def getDataStructure(self, params):
		"""
		Creates the data tree from e-class tables
		:param params Includes input parameters such as filters, etc.
		"""
		filters = params['filters']
		structure = {}
		cls = self.getClasses(filters)

		for cl in cls:
			_cl = mdl.createClassDict(cl)
			prs = self.getProperties(_cl[ec_str['class']['id']], filters)
			if not prs:
				structure = prepareStructure(structure, _cl, [], [], [])
				continue
			for pr in prs:
				_pr = mdl.createPropertyDict(pr)
				vas = self.getValues(_pr[ec_str['property']['id']], filters)
				_vas = []
				for va in vas:
					_vas.append(mdl.createValueDict(va))
				uns = self.getUnits(_pr[ec_str['property']['id']], filters)
				_uns = []
				for un in uns:
					_uns.append(mdl.createUnitDict(un))
				structure = prepareStructure(structure, _cl, _pr, _vas, _uns)

		array = convertStructureToArray(structure)
		return array

	def getFields(self):
		"""
		Gets column names of e-class tables
		"""
		result = {}
		result['cl'] = getColumnNames(ec_str['class']['table'])
		result['pr'] = getColumnNames(ec_str['property']['table'])
		result['va'] = getColumnNames(ec_str['value']['table'])
		result['un'] = getColumnNames(ec_str['unit']['table'])
		return result


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
			'name': cl[ec_str['class']['name']],
			'children': {},
		}

	""" If property has no item, then return """
	if ec_str['property']['id'] not in pr:
		return structure

	""" Adding property as the class child """
	structure[cl[ec_str['class']['id']]]['children'][pr[ec_str['property']['id']]] = {
		'data': pr,
		'name': pr[ec_str['property']['name']],
		'children': {},
	}

	""" Adding value as the property child """
	structure[cl[ec_str['class']['id']]]['children'][pr[ec_str['property']['id']]]['children']['value'] = {
		'data': vas,
		'name': 'value',
	}

	""" Adding unit as the property child """
	structure[cl[ec_str['class']['id']]]['children'][pr[ec_str['property']['id']]]['children']['unit'] = {
		'data': uns,
		'name': 'unit',
	}

	# print(structure)

	return structure


def setFilters(query, filters, _type, alias):
	if _type not in filters:
		return query
	if filters[_type]['v'] and filters[_type]['q']:
		query += " and ("
		for field in getColumnNames(ec_str[_type]['table']):
			query += " {}.{} like '%{}%' or".format(alias, field['col'], filters[_type]['q'])
		""" To remove last extra ' or' """
		query = query[:-3] + ")"
	return query


def getColumnNames(table_name):
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


def convertStructureToArray(structure):
	"""
	Converts structure object to array for easier process in front
	:param structure
	"""
	array = []
	i = 0
	j = 0
	for cl in structure:
		_cl = structure[cl]
		array.append({
			'data': _cl['data'],
			'name': _cl['name'],
			'children': [],
		})
		if not bool(_cl['children']):
			continue
		for pr in _cl['children']:
			_pr = _cl['children'][pr]
			array[i]['children'].append({
				'data': _pr['data'],
				'name': _pr['name'],
				'children': [],
			})
			for child in _pr['children']:
				_child = _pr['children'][child]
				array[i]['children'][j]['children'].append({
					'data': _child['data'],
					'name': _child['name'],
				})
			j = j + 1
		j = 0
		i = i + 1
	return array
