# -*- coding: utf-8 -*-
import functools
import json

from Crypto.Cipher import AES
from exceptions import XakoLangException
from swagger.rsp import error


def lang(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
            return result
        except XakoLangException:
            return error(40002, 'no language "%s" supported' % kwargs['lang']), 400
    return wrapper
