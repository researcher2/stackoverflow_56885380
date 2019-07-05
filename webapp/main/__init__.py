def create_module(app):
    from .controller import blueprint
    app.register_blueprint(blueprint)