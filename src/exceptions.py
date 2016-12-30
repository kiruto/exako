# -*- coding: utf-8 -*-
class XVersionNotFoundException(ValueError):
    """
    Try to use a wrong version value.
    """
    pass


class XRoutingException(Exception):
    """
    Routing helper exception
    """


class XakoException(Exception):
    """
    Known errors
    """


class XakoLangException(XakoException):
    def __init__(self, *args, **kwargs):
        super().__init__('Language support error', *args, **kwargs)
