from eclass.dao import EclassDao

db = EclassDao()
# db.initialize_db()
db.getFromTable('eClass7_1_CC_en_01_190102xx')
