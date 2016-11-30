# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


try:
    import local_properties
    from raven.contrib.flask import Sentry
    sentry = Sentry(app, dsn=local_properties.SENTRY_DSN)
except ImportError as msg:
    print(msg)
    print('cannot connect to sentry')


@app.route('/')
def hp():
    return 'hello exako'
