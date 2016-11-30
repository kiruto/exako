# -*- coding: utf-8 -*-
import database
from database.ako_data import AkoData

database.exec_sql_file('tag_create_table.sql')


class Tag(AkoData):
    pass
