# -*- coding: utf-8 -*-
import os

CURRENT_PATH = os.path.dirname(__file__) + os.sep


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


STATIC_PATH = get_or_create('static')
TEMPLATE_PATH = get_or_create('template')
CACHE_PATH = get_or_create('..', 'cache')
DATA_PATH = get_or_create('..', 'data')
