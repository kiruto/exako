# -*- coding: utf-8 -*-
from flask import Flask

from routing import RoutingHelper

app = Flask(__name__)
routing = RoutingHelper(app)


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


def depth_0_1():
    return '0,1'


def depth_0_2():
    return '0,2'


def depth_1_0():
    return '1,0'


def depth_1_1():
    return '1,1'


@routing.args('/<path:path>', methods=['GET'])
def depth_2_0(path):
    return '2,0' + path


routing_tree = {
    'route_depth_0_0': {
        'route_depth_1_0': depth_1_0,
        'route_depth_1_1': depth_1_1
    },
    'route_depth_0_1': {
        'route_depth_1_0': {
            'route_depth_2_0': depth_2_0
        }
    }
}
routing.tree(**routing_tree)
