from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(app):


    app=(__name__)


    db.init_app(app)

    #registering bluebrint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')


    # setting config
    from .requests import configure_request
    configure_request(app)

    return app




    


