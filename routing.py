# -*- coding: utf-8 -*-

from flask import Flask
from werkzeug.routing import Rule

from exceptions import XRoutingException


class RoutingHelper:

    def __init__(self, app: Flask):
        self._app = app

    def redirect_list(self, *args: str):

        def decorator(fun):
            for path_string in args:
                defaults = None if ('<path:path>' in path_string) else {'path': None}
                self._app.route(path_string, defaults=defaults)(RouteFunctionWrapper(fun))
            return
        return decorator

    def tree(self, current_path='', **kwargs):
        for path, item in kwargs.items():
            this_path = current_path + '/' + path
            if callable(item):
                self._app.route(this_path)(RouteFunctionWrapper(item))
            elif isinstance(item, list):
                if len(item) == 2 and callable(item[0]) and isinstance(item[1], dict):
                    self._app.route(this_path, **item[1])(RouteFunctionWrapper(item[0]))
                else:
                    raise XRoutingException(
                        'Routing tree array must contains routing function and routing arguments dict.'
                    )
            elif isinstance(item, tuple):
                if len(item) == 3 and callable(item[0]) and isinstance(item[1], str) and isinstance(item[2], dict):
                    self._app.route(this_path + item[1], **item[2])(RouteFunctionWrapper(item[0]))
            elif isinstance(item, dict):
                self.tree(this_path, **item)

    def args(self, rule='', **options: {
        'string: str': '',
        'endpoint: str': Rule.endpoint,
        'defaults: str': Rule.defaults,
        'subdomain: str': Rule.subdomain,
        'methods: str': Rule.methods,
        'strict_slashes: str': Rule.strict_slashes,
        'build_only: str': Rule.build_only,
        'redirect_to: str': Rule.redirect_to,
        'alias: str': Rule.alias,
        'host: str': Rule.host
    }):
        def decorator(fun):
            return fun, rule, options
        return decorator


class RouteFunctionWrapper:
    def __init__(self, function):
        self.fun = function
        self.__name__ = 'route_function%i' % id(self)

    def __call__(self, **kwargs):
        return self.fun(**kwargs)
