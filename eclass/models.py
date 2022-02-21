from eclass.settings import ec_str, Eclass


class Models:

	def createClassDict(self, cl_object):
		"""
		This method converts e-class object to e-class json
		:param cl_object Is the e-class object resulted from db fetch command
		"""
		if hasattr(cl_object, ec_str[Eclass.CL]['id']) is False:
			return {}
		return {
			'Supplier': cl_object.Supplier,
			'IdCC': cl_object.IdCC,
			'Identifier': cl_object.Identifier,
			'VersionNumber': cl_object.VersionNumber,
			'VersionDate': cl_object.VersionDate,
			'RevisionNumber': cl_object.RevisionNumber,
			'CodedName': cl_object.CodedName,
			'PreferredName': cl_object.PreferredName,
			'Definition': cl_object.Definition,
			'ISOLanguageCode': cl_object.ISOLanguageCode,
			'ISOCountryCode': cl_object.ISOCountryCode,
			'Note': cl_object.Note,
			'Remark': cl_object.Remark,
			'Level': cl_object.Level,
			'MKSubclass': cl_object.MKSubclass,
			'MKKeyword': cl_object.MKKeyword,
			'MKBSA': cl_object.MKBSA,
			'IrdiCC': cl_object.IrdiCC,
		}

	def createPropertyDict(self, pr_object):
		"""
		This method converts property object to property json
		:param pr_object Is the property object resulted from db fetch command
		"""
		if hasattr(pr_object, ec_str[Eclass.PR]['id']) is False:
			return {}
		return {
			'Supplier': pr_object.Supplier,
			'IdPR': pr_object.IdPR,
			'Identifier': pr_object.Identifier,
			'VersionNumber': pr_object.VersionNumber,
			'VersionDate': pr_object.VersionDate,
			'RevisionNumber': pr_object.RevisionNumber,
			'PreferredName': pr_object.PreferredName,
			'ShortName': pr_object.ShortName,
			'Definition': pr_object.Definition,
			'Note': pr_object.Note,
			'Remark': pr_object.Remark,
			'FormularSymbol': pr_object.FormularSymbol,
			'IrdiUN': pr_object.IrdiUN,
			'ISOLanguageCode': pr_object.ISOLanguageCode,
			'ISOCountryCode': pr_object.ISOCountryCode,
			'Category': pr_object.Category,
			'AttributeType': pr_object.AttributeType,
			'Reference': pr_object.Reference,
			'DefinitionClass': pr_object.DefinitionClass,
			'DataType': pr_object.DataType,
			'DigitsBeforeComma': pr_object.DigitsBeforeComma,
			'DigitsAfterComma': pr_object.DigitsAfterComma,
			'NumberOfCharacters': pr_object.NumberOfCharacters,
			'IrdiPR': pr_object.IrdiPR,
			'CurrencyAlphaCode': pr_object.CurrencyAlphaCode,
		}

	def createValueDict(self, va_object):
		"""
		This method converts value object to value json
		:param va_object Is the value object resulted from db fetch command
		"""
		if hasattr(va_object, ec_str[Eclass.VA]['id']) is False:
			return {}
		return {
			'Supplier': va_object.Supplier,
			'IdVA': va_object.IdVA,
			'Identifier': va_object.Identifier,
			'VersionNumber': va_object.VersionNumber,
			'RevisionNumber': va_object.RevisionNumber,
			'VersionDate': va_object.VersionDate,
			'PreferredName': va_object.PreferredName,
			'ShortName': va_object.ShortName,
			'Definition': va_object.Definition,
			'Reference': va_object.Reference,
			'ISOLanguageCode': va_object.ISOLanguageCode,
			'ISOCountryCode': va_object.ISOCountryCode,
			'IrdiVA': va_object.IrdiVA,
			'DataType': va_object.DataType,
		}

	def createUnitDict(self, un_object):
		"""
		This method converts unit object to unit json
		:param un_object Is the unit object resulted from db fetch command
		"""
		if hasattr(un_object, ec_str[Eclass.UN]['id']) is False:
			return {}
		return {
			'StructuredNaming': un_object.StructuredNaming,
			'ShortName': un_object.ShortName,
			'Definition': un_object.Definition,
			'Source': un_object.Source,
			'Comment': un_object.Comment,
			'SINotation': un_object.SINotation,
			'SIName': un_object.SIName,
			'DINNotation': un_object.DINNotation,
			'ECEName': un_object.ECEName,
			'ECECode': un_object.ECECode,
			'NISTName': un_object.NISTName,
			'IECClassification': un_object.IECClassification,
			'IrdiUN': un_object.IrdiUN,
			'NameOfDedicatedQuantity': un_object.NameOfDedicatedQuantity,
		}

# class eClass7_1_CC_en_01_190102xx(models.Model):
# 	Supplier = models.CharField(max_length=6)
# 	IdCC = models.CharField(max_length=9)
# 	Identifier = models.CharField(max_length=6)
# 	VersionNumber = models.FloatField(default=0)
# 	VersionDate = models.DateTimeField(null=True)
# 	RevisionNumber = models.FloatField(default=0)
# 	CodedName = models.FloatField(default=0)
# 	PreferredName = models.TextField(null=True)
# 	Definition = models.TextField(default='---empty---')
# 	ISOLanguageCode = models.CharField(max_length=2)
# 	ISOCountryCode = models.CharField(max_length=2)
# 	Note = models.TextField(default='---empty---')
# 	Remark = models.TextField(default='---empty---')
# 	Level = models.FloatField(default=0)
# 	MKSubclass = models.FloatField(default=0)
# 	MKKeyword = models.FloatField(default=0)
# 	MKBSA = models.FloatField(null=True)
# 	IrdiCC = models.CharField(max_length=20)
# 	objects = models.Manager()
