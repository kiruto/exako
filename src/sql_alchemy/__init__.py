# -*- coding: utf-8 -*-
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
