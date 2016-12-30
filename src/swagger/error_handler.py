# -*- coding: utf-8 -*-
from connexion import problem
from connexion.handlers import ResolverErrorHandler

from exceptions import XakoLangException


class ErrorHandler(ResolverErrorHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **kwargs):
        if isinstance(self.exception, XakoLangException):
            return problem(title='Not Implemented', detail='', status=self.status_code)
