# -*- coding: utf-8 -*-
import logging
import pathlib

from connexion.resolver import Resolver

from connexion.api import Api

import config
__version__ = '1.0'
swagger_file = 'swagger.yaml'


def init_connexion(app):

    logger = logging.getLogger('connexion.app')
    root_path = pathlib.Path(app.root_path)

    specification_dir = pathlib.Path('./swagger')  # Ensure specification dir is a Path
    if specification_dir.is_absolute():
        specification_dir = specification_dir
    else:
        specification_dir = root_path / specification_dir

    logger.debug('Specification directory: %s', specification_dir)

    def resolver_error_handler(*args, **kwargs):
        kwargs['operation'] = {
            'operationId': 'connexion.handlers.ResolverErrorHandler',
        }
        kwargs.setdefault('app_consumes', ['application/json'])
        from swagger.error_handler import ErrorHandler
        return ErrorHandler(400, *args, **kwargs)

    resolver = Resolver()
    resolver = Resolver(resolver) if hasattr(resolver, '__call__') else resolver

    swagger_json = True
    swagger_ui = True
    swagger_path = None
    swagger_url = None
    auth_all_paths = False
    logger.debug('Adding API: %s', swagger_file)

    arguments = {'title': 'exako api'}
    yaml_path = specification_dir / swagger_file
    api = Api(swagger_yaml_path=yaml_path,
              base_url=None, arguments=arguments,
              swagger_json=swagger_json,
              swagger_ui=swagger_ui,
              swagger_path=swagger_path,
              swagger_url=swagger_url,
              resolver=resolver,
              resolver_error_handler=resolver_error_handler,
              validate_responses=config.DEBUG and not config.ENCRYPT,
              strict_validation=False,
              auth_all_paths=auth_all_paths,
              debug=False)
    app.register_blueprint(api.blueprint)
    return api
