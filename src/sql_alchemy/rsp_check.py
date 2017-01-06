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


def aes_dict(function):
    """
    AES crypto by pycrypto 2.6.1
    https://pypi.python.org/pypi/pycrypto
    :param function:
    :return:
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        try:
            from local_properties import AES_KEY, AES_IV
        except:
            return result
        data = json.dumps(result)
        aes = AES.new(AES_KEY, AES.MODE_CFB, AES_IV)
        return aes.encrypt(data).decode(encoding='utf16')
    return wrapper
