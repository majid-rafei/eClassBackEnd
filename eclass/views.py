from django.views import View
from eclass.eclass_dao import EclassDao
from django.http import JsonResponse


class EclassViews(View):
	"""
	This class maintains e-class endpoints
	"""

	def getDataStructure(self, request):
		"""
		This endpoint is intended for getting whole e-class data as a tree, which shows relations
		:param request Is the request object.
		"""
		dao = EclassDao()
		params = {}
		params['filters'] = {}
		data = dao.getDataStructure(params)
		return JsonResponse(data, safe=False)

	def getFields(self, request):
		"""
		This endpoint is intended for getting fields of e-class tables: Class, Property, Value, Unit
		:param request Is the request object.
		"""
		dao = EclassDao()
		data = dao.getFields()
		return JsonResponse(data)
