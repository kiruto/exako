# -*- coding: utf-8 -*-
from swagger.error_code import error_code


def error(code, msg):
    return {
        'code': code,
        'msg': error_code.get(code, 'Unknown error'),
        'err': msg
    }
