# -*- coding: utf-8 -*-
from src.exceptions import XVersionNotFoundException

latest_version = None

_version = list()


class Version:
    def __init__(self, name=latest_version.name, code=latest_version.code):
        self.name = name
        self.code = code

    def __cmp__(self, other):
        return self.code - other.code


def find_version_by_name(name: '0.0.1') -> Version:
    for v in _version:
        if v.name == name:
            return v
    raise XVersionNotFoundException


def find_version_by_code(code: 1) -> Version:
    for v in _version:
        if v.code == code:
            return v
    raise XVersionNotFoundException


def register_version(version: Version=None, code: 1=None, name: '0.0.1'=None):
    v = None
    if version:
        v = version
    elif code:
        v = find_version_by_code(code)
    elif name:
        v = find_version_by_name(name)
    _version.append(v)
    global latest_version
    if latest_version < v:
        latest_version = v

