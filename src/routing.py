# -*- coding: utf-8 -*-
import json

from flask import request

import environment
from flask import Flask
from werkzeug.routing import Rule

import protobuf
import runtime_context
import sql_alchemy
from exceptions import XRoutingException
from protobuf import database_pb2
from protobuf import rest_request_pb2
from rest.request import parse_request_dict
from rest.response import parse_buf, proto_response
from sql_alchemy.databases import AkoSiteMeta, AkoLang, AkoMetaValue

URL_MAPPING_FILE = environment.get_file('route_map.txt')


class RoutingHelper:
    def __init__(self, app: Flask):
        self._app = app
        self._mapping = ''

    def redirect_list(self, *args: str):

        def decorator(fun):
            for path_string in args:
                defaults = None if ('<path:path>' in path_string) else {'path': None}
                self._map(path_string, fun, defaults=defaults)
            return

        return decorator

    def tree(self, current_path='', **kwargs):
        for path, item in kwargs.items():
            this_path = current_path + '/' + path
            if callable(item):
                self._map(this_path, item)
            elif isinstance(item, list):
                if len(item) == 2 and callable(item[0]) and isinstance(item[1], dict):
                    self._map(this_path, item[0], **item[1])
                else:
                    raise XRoutingException(
                        'Routing tree array must contains routing function and routing arguments dict.'
                    )
            elif isinstance(item, tuple):
                if len(item) == 3 and callable(item[0]) and isinstance(item[1], str) and isinstance(item[2], dict):
                    self._map(this_path + item[1], item[0], **item[2])
            elif isinstance(item, dict):
                self.tree(this_path, **item)

    def args(self, rule='', **options: {
        'string: str': '',
        'endpoint: str': 'Rule.endpoint',
        'defaults: str': 'Rule.defaults',
        'subdomain: str': 'Rule.subdomain',
        'methods: str': 'Rule.methods',
        'strict_slashes: str': 'Rule.strict_slashes',
        'build_only: str': 'Rule.build_only',
        'redirect_to: str': 'Rule.redirect_to',
        'alias: str': 'Rule.alias',
        'host: str': 'Rule.host'
    }):
        def decorator(fun):
            return fun, rule, options

        return decorator

    def _map(self, rule: str, fun, **options):
        self._mapping += '{path}\t{module}.{name}\n'.format(path=rule, module=fun.__module__, name=fun.__name__)
        self._app.route(rule, **options)(RouteFunctionWrapper(fun))

    def save_mapping_info(self):
        with open(URL_MAPPING_FILE, 'w') as file:
            file.write(self._mapping)
            file.close()


class RouteFunctionWrapper:
    def __init__(self, function):
        self.fun = function
        self.__name__ = 'route_function%i' % id(self)

    def __call__(self, **kwargs):
        return self.fun(**kwargs)


def init_app(app):

    routing = RoutingHelper(app)

    def request_arg():
        arg = request.args.get('buf')
        request_dict = {}
        if arg:
            arg = rest_request_pb2.Request.ParseFromString(arg)
            request_dict = parse_request_dict(request_arg)
        return arg, request_dict

    def lang(lang: str):
        for l in runtime_context.langs:
            if lang == l.name:
                return l
        return None

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

    def site_meta():
        print(request_arg)
        l = 'en'
        arg, arg_dict = request_arg()
        if 'lang' in request_arg():
            l = arg_dict['lang']
            print(arg_dict['lang'])

        meta = AkoMetaValue.query.filter_by(lang=lang(l)).all()
        contents = []
        for m in meta:
            contents.append(parse_buf(database_pb2.Meta(), name=m.meta_info.name, value=m.value, lang=str(m.lang)))
        return proto_response(contents)

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
        },
        'rest': {
            'meta': site_meta
        }
    }
    routing.tree(**routing_tree)
    routing.save_mapping_info()
