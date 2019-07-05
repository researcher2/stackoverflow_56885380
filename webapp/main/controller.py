from flask import Blueprint, render_template, current_app as app
from .models import MyTable

from webapp import db

blueprint = Blueprint('main', __name__)

@blueprint.route('/')
def index():
    results = db.session.query(MyTable).all()
    print(results)
    for row in results:
        print (row)  
        print(row.versions)
        print(row.name)

    if results:
        return render_template('my_table.html', results=results)
    else:
        return 'Nothing happend'