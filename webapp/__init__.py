from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_object):
    app=Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    db.reflect(bind="sample_bind", app=app)

    from webapp.main import create_module as main_create_module
    main_create_module(app)

    return app