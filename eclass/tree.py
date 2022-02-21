from eclass.settings import ec_str, Eclass
from eclass.models import Models
from eclass.dao import EclassDao


class Tree:

	def getFields(self):
		"""
		Gets column names of e-class tables
		"""
		dao = EclassDao()
		result = {}
		result['cl'] = dao.getColumnNames(ec_str[Eclass.CL]['table'])
		result['pr'] = dao.getColumnNames(ec_str[Eclass.PR]['table'])
		result['va'] = dao.getColumnNames(ec_str[Eclass.VA]['table'])
		result['un'] = dao.getColumnNames(ec_str[Eclass.UN]['table'])
		return result

	def getDataStructure(self, params):
		"""
		Creates the data tree from e-class tables
		:param params Includes input parameters such as filters, etc.
		"""
		filters = params['filters']
		structure = {}
		dao = EclassDao()
		cls = dao.getClasses(filters)
		mdl = Models()

		for cl in cls:
			_cl = mdl.createClassDict(cl)
			cl_id = ec_str[Eclass.CL]['id']
			prs = dao.getProperties(_cl[cl_id], filters)
			if not prs:
				structure = self.prepareStructure(structure, _cl, [], [], [])
				continue
			for pr in prs:
				_pr = mdl.createPropertyDict(pr)
				pr_id = ec_str[Eclass.PR]['id']
				vas = dao.getValues(_pr[pr_id], filters)
				_vas = []
				for va in vas:
					_vas.append(mdl.createValueDict(va))
				uns = dao.getUnits(_pr[pr_id], filters)
				_uns = []
				for un in uns:
					_uns.append(mdl.createUnitDict(un))
				structure = self.prepareStructure(structure, _cl, _pr, _vas, _uns)

		array = self.convertStructureToArray(structure)
		return array

	def prepareStructure(self, structure, cl, pr, vas, uns):
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

		cl_id = ec_str[Eclass.CL]['id']

		""" If structure has not the class key, then it is added """
		if cl[cl_id] not in structure:
			structure[cl[cl_id]] = {
				'data': cl,
				'name': cl[ec_str[Eclass.CL]['name']],
				'children': {},
			}

		pr_id = ec_str[Eclass.PR]['id']

		""" If property has no item, then return """
		if pr_id not in pr:
			return structure

		""" Adding property as the class child """
		structure[cl[cl_id]]['children'][pr[pr_id]] = {
			'data': pr,
			'name': pr[ec_str[Eclass.PR]['name']],
			'children': {},
		}

		""" Adding value as the property child """
		structure[cl[cl_id]]['children'][pr[pr_id]]['children'][Eclass.VA] = {
			'data': vas,
			'name': Eclass.VA,
		}

		""" Adding unit as the property child """
		structure[cl[cl_id]]['children'][pr[pr_id]]['children'][Eclass.UN] = {
			'data': uns,
			'name': Eclass.UN,
		}

		# print(structure)

		return structure

	def convertStructureToArray(self, structure):
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
