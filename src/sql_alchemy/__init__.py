# -*- coding: utf-8 -*-
import json

from sqlalchemy import event

import database
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta

db = SQLAlchemy()
table_create_scripts = dict()


class ModelConfig:
    def __init__(self, cls, file=None, script=None):
        self.cls = cls
        self.file = file
        self.script = script
        self()

    def __call__(self, *args, **kwargs):
        if self.file:
            database.exec_sql_file(self.file)
        if self.script:
            database.exec_blocks(self.script)


def create_table(file_name: str=None, script: str=None):
    """
    Create table with sql file before SQLA class
    :param file_name: sql file
    :param script: sql script string
    :return:
    """
    def _decorator(cls):
        if cls.__name__ not in table_create_scripts:
            config = ModelConfig(cls, file_name, script)
            table_create_scripts[cls.__name__] = config
        elif not table_create_scripts[cls.__name__].file:
            table_create_scripts[cls.__name__].file = file_name
            table_create_scripts[cls.__name__].script = script
        return cls
    return _decorator


def alchemy_encoder(revisit_self=False, fields_to_expand=()):
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if revisit_self:
                    if obj in _visited_objs:
                        return None
                    _visited_objs.append(obj)

                # go through each field in this SQLalchemy class
                fields = {}
                for field in [x for x in dir(obj) if
                              not x.startswith('_') and x != 'metadata' and not x.startswith('query')]:
                    val = obj.__getattribute__(field)

                    # is this field another SQLalchemy object, or a list of SQLalchemy objects?
                    if isinstance(val.__class__, DeclarativeMeta) or (isinstance(val, list) and len(val) > 0 and isinstance(val[0].__class__, DeclarativeMeta)):
                        # unless we're expanding this field, stop here
                        if field not in fields_to_expand:
                            # not expanding this field: set it to None and continue
                            fields[field] = None
                            continue

                    fields[field] = val
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)
    return AlchemyEncoder


def to_json(obj, fields_to_expand=()):
    """
    Convert a SQLA object to json string
    :param obj:
    :param fields_to_expand:
    :return:
    """
    return json.dumps(obj, cls=alchemy_encoder(False, fields_to_expand), check_circular=False)
