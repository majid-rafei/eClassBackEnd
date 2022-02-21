from django.views import View
from eclass.tree import Tree
from django.http import JsonResponse
import json
from types import SimpleNamespace
from eclass.settings import Eclass


class EclassViews(View):
	"""
	This class maintains e-class endpoints
	"""

	def getDataStructure(self, request):
		"""
		This endpoint is intended for getting whole e-class data as a tree, which shows relations too.
		:param request Is the request object.
		"""
		tree = Tree()
		params = {}
		if request.GET.get('filters'):
			_filters = json.loads(request.GET.get('filters'), object_hook=lambda d: SimpleNamespace(**d))
			filters = {'tx': _filters.tx, Eclass.CL: {
				'c': _filters.cl.c,
				'q': _filters.cl.q,
			}, Eclass.PR: {
				'c': _filters.pr.c,
				'q': _filters.pr.q,
			}, Eclass.VA: {
				'c': _filters.va.c,
				'q': _filters.va.q,
			}, Eclass.UN: {
				'c': _filters.un.c,
				'q': _filters.un.q,
			}}
			params['filters'] = filters
		else:
			params['filters'] = {}
		data = tree.getDataStructure(params)
		return JsonResponse(data, safe=False)

	def getFields(self, request):
		"""
		This endpoint is intended for getting fields of e-class tables: Class, Property, Value, Unit
		:param request Is the request object.
		"""
		tree = Tree()
		data = tree.getFields()
		return JsonResponse(data)
