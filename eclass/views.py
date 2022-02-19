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
		data = dao.getDataStructure()
		return JsonResponse(data)
