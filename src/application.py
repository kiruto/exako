# -*- coding: utf-8 -*-
from flask import Flask
import config

from config import MARIA_USER, MARIA_PASSWORD, MARIA_SERVER, MARIA_DATABASE


def application():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://%s:%s@%s:3306/%s?charset=utf8" % (MARIA_USER,
                                                                                       MARIA_PASSWORD,
                                                                                       MARIA_SERVER,
                                                                                       MARIA_DATABASE)
    app.config['SQLALCHEMY_ECHO'] = config.DEBUG
    app.config['SECRET_KEY'] = '123456790'

    try:
        import local_properties
        from raven.contrib.flask import Sentry

        sentry = Sentry(app, dsn=local_properties.SENTRY_DSN)
    except Exception as msg:
        print(msg)
        print('cannot connect to sentry')

    @app.after_request
    def apply_allow_origin(response):
        if config.DEBUG:
            response.headers['Access-Control-Allow-Origin'] = '*'
        return response

    return app
