# -*- coding: utf-8 -*-
import os

DEBUG = True
RELEASE = not DEBUG
CURRENT_PATH = os.path.dirname(__file__) + os.sep
SQL = 'sql'


def get_dir(*paths):
    return os.path.join(CURRENT_PATH, *paths) + os.sep


def get_file(*paths):
    return os.path.join(CURRENT_PATH, *paths)


def get_or_create(*paths):
    abs_path = get_dir(*paths)
    if not os.path.exists(abs_path):
        os.makedirs(abs_path)
    return abs_path


def create(*paths):
    """
    Returns a path and create if not exist.
    """
    abs_path = get_or_create(*paths)

    def decorator(fun):
        return fun(abs_path)
    return decorator


SQL_PATH = get_dir(SQL)


def get_sql_file(file_name: str):
    return get_file('sql', file_name)


STATIC_PATH = get_or_create('static')
TEMPLATE_PATH = get_or_create('template')
CACHE_PATH = get_or_create('..', 'cache')
DATA_PATH = get_or_create('..', 'data')
