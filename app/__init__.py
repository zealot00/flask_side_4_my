#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'

from flask import Flask, render_template
#from flask.ext.bootstrap import Bootstrap
from flask_bootstrap import Bootstrap
#from flask.ext.mail import Mail
from flask_mail import Mail
#from flask.ext.moment import Moment
from flask_moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # attach routes and custom error pages here
    from api import api as api_bluepoint
    from home import home as home_bluepoint


    app.register_blueprint(api_bluepoint,url_prefix='/api')
    app.register_blueprint(home_bluepoint,url_prefix='/home')


    return app