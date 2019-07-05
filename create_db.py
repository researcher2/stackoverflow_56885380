from sqlalchemy import Column, String, Integer

from webapp import db, create_app

import os

class MyTable(db.Model):
    __bind_key__ = 'sample_bind'
    __tablename__ = "my_table"

    id = Column(Integer, primary_key=True)
    versions = Column(String(255))
    name = Column(String(255))

try:
    os.remove("webapp/sample.db")
except:
    pass

app = create_app("config.Config")

with app.app_context():

    db.create_all(bind=['sample_bind'], app=app)

    row1 = MyTable()
    row1.versions = "1"
    row1.name = "The First Version"

    row2 = MyTable()
    row2.versions = "1.1"
    row2.name = "The First Version With Lots Of BugFix"

    db.session.add(row1)
    db.session.add(row2)
    db.session.commit()
