# -*- coding: utf-8 -*-
import logging
import pathlib

from connexion.resolver import Resolver

from connexion.api import Api

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

    def resolver_error_handler(self, *args, **kwargs):
        from connexion.handlers import ResolverErrorHandler
        kwargs['operation'] = {
            'operationId': 'connexion.handlers.ResolverErrorHandler',
        }
        kwargs.setdefault('app_consumes', ['application/json'])
        return ResolverErrorHandler(self.resolver_error, *args, **kwargs)

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
              validate_responses=False,
              strict_validation=False,
              auth_all_paths=auth_all_paths,
              debug=False)
    app.register_blueprint(api.blueprint)
    return api
