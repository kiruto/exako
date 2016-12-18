# -*- coding: utf-8 -*-
import json

from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy import Column
# from sqlalchemy import Integer
# from sqlalchemy import MetaData
# from sqlalchemy import String
# from sqlalchemy import TIMESTAMP
# from sqlalchemy import Table
# from sqlalchemy import Text
# from sqlalchemy import create_engine
#
# from config import MARIA_USER, MARIA_PASSWORD, MARIA_SERVER, MARIA_DATABASE
from sqlalchemy.ext.declarative import DeclarativeMeta

db = SQLAlchemy()

# engine = create_engine("mysql://%s:%s@%s:3306/%s?charset=utf8" % (MARIA_USER, MARIA_PASSWORD, MARIA_SERVER, MARIA_DATABASE)
#                        , encoding="utf-8", echo=True)
# metadata = MetaData()
# table_activity = Table('ako_activity', metadata,
#                        Column('id', Integer, primary_key=True),
#                        Column('platform', String),
#                        Column('source_url', Text),
#                        Column('create_at', TIMESTAMP),
#                        Column('title', Text),
#                        Column('description', Text),
#                        Column('thumbnail_url', Text),
#                        Column('tag', String),
#                        Column('extra', Text))
# table_site_meta = Table('ako_tag', metadata,
#                         Column('id', Integer, primary_key=True),
#                         Column('name', String),
#                         Column('extra', Text))
# conn = engine.connect()


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
    return json.dumps(obj, cls=alchemy_encoder(False, fields_to_expand), check_circular=False)
