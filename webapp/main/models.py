from webapp import db

class MyTable(db.Model):
    __bind_key__ = 'sample_bind'
    __table__ = db.metadata.tables['my_table']