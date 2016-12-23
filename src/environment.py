# -*- coding: utf-8 -*-
import os

import time

from config import GIT_RAW_FILE_CDN

DEBUG = True
RELEASE = not DEBUG
CURRENT_PATH = os.path.dirname(__file__)
if not CURRENT_PATH:
    CURRENT_PATH = os.getcwd() + os.sep
else:
    CURRENT_PATH += os.sep
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


def append(root_path, path):
    return root_path + path + os.sep


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

_GIT_PATH_ROOT = ('..', '..')
_GIT_DIST_REPO_NAME = ('exako-static', )
_GIT_DIST_REPO_IMAGE_PATH = ('img', )
STATIC_DIST_GIT_PATH = get_or_create(*(_GIT_PATH_ROOT + _GIT_DIST_REPO_NAME))
STATIC_DIST_GIT_IMAGE_PATH = get_or_create(*(_GIT_PATH_ROOT + _GIT_DIST_REPO_NAME + _GIT_DIST_REPO_IMAGE_PATH))


def get_image_upload_path():
    return time.strftime('%Y%m', time.localtime(time.time()))


def get_abs_image_upload_path():
    t = get_image_upload_path()
    path = get_or_create(STATIC_DIST_GIT_IMAGE_PATH, t)
    return path


def get_raw_file_url(*args):
    'img/201612/2016_12_23-15_45_45-b_j1mwo4_400x400.png'
    return GIT_RAW_FILE_CDN + ('/'.join(args))


def get_raw_image_url(model):
    return get_raw_file_url('img', model.path, model.name)
