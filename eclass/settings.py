class Eclass():
	CL = 'class'
	PR = 'property'
	VA = 'value'
	UN = 'unit'

"""
Structure of the e-class data
"""
ec_str = {
	Eclass.CL: {
		'parent': {},
		'children': {
			Eclass.PR: {
				'relation': 'eClass7_1_CC_PR_en_01_190102xx',
			}
		},
		'table': 'eClass7_1_CC_en_01_190102xx',
		'id': 'IrdiCC',
		'name': 'PreferredName',
	},
	Eclass.PR: {
		'parent': Eclass.CL,
		'children': {
			Eclass.VA: {
				'relation': 'eClass7_1_PR_VA_restricted_en_01_190102xx'
			},
			Eclass.UN: {
				'relation': 'eClass7_1_PR_en_01_190102xx'
			},
		},
		'table': 'eClass7_1_PR_en_01_190102xx',
		'id': 'IrdiPR',
		'name': 'PreferredName',
	},
	Eclass.VA: {
		'parent': Eclass.PR,
		'children': {},
		'table': 'eClass7_1_VA_en_01_190102xx',
		'id': 'IrdiVA',
		'name': 'PreferredName',
	},
	Eclass.UN: {
		'parent': Eclass.PR,
		'children': {},
		'table': 'eClass7_1_UN_en_01_190102xx',
		'id': 'IrdiUN',
		'name': 'StructuredNaming',
	}
}
