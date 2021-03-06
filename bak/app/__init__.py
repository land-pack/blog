from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.pagedown import PageDown
from config import config
# from log import create_logger

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
pagedown = PageDown()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    # login_manager.init_app(app)
    pagedown.init_app(app)

    from blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')
    #
    # from .gallery import gallery as gallery_blueprint
    # app.register_blueprint(gallery_blueprint, url_prefix='/gallery')

    # attach routes and custom error pages here


    # addHandler to app
    # import logging
    # handler = create_logger('/var/log/gallery.log', level=logging.INFO)
    # app.logger.addHandler(handler)
    return app
