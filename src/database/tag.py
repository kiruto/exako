# -*- coding: utf-8 -*-
import database

from src.database.ako_data import AkoData

database.exec_sql_file('tag_create_table.sql')


class Tag(AkoData):
    def __init__(self):
        super().__init__()
