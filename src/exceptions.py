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