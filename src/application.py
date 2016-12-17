# -*- coding: utf-8 -*-
from flask import Flask

from config import MARIA_USER, MARIA_PASSWORD, MARIA_SERVER, MARIA_DATABASE

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://%s:%s@%s:3306/%s?charset=utf8" % (MARIA_USER,
                                                                                   MARIA_PASSWORD,
                                                                                   MARIA_SERVER,
                                                                                   MARIA_DATABASE)
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = '123456790'

try:
    import local_properties
    from raven.contrib.flask import Sentry

    sentry = Sentry(app, dsn=local_properties.SENTRY_DSN)
except ImportError as msg:
    print(msg)
    print('cannot connect to sentry')
