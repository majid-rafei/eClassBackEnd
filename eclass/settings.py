"""
Structure of the e-class data
"""
ec_str = {
	'class': {
		'parent': {},
		'children': {
			'property': {
				'relation': 'eClass7_1_CC_PR_en_01_190102xx',
			}
		},
		'table': 'eClass7_1_CC_en_01_190102xx',
		'id': 'IrdiCC',
	},
	'property': {
		'parent': 'class',
		'children': {
			'value': {
				'relation': 'eClass7_1_PR_VA_restricted_en_01_190102xx'
			},
			'unit': {
				'relation': 'eClass7_1_PR_en_01_190102xx'
			},
		},
		'table': 'eClass7_1_PR_en_01_190102xx',
		'id': 'IrdiPR',
	},
	'value': {
		'parent': 'property',
		'children': {},
		'table': 'eClass7_1_VA_en_01_190102xx',
		'id': 'IrdiVA',
	},
	'unit': {
		'parent': 'property',
		'children': {},
		'table': 'eClass7_1_UN_en_01_190102xx',
		'id': 'IrdiUN',
	}
}
