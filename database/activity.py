# -*- coding: utf-8 -*-
import database
from database.ako_data import AkoData

database.exec_sql_file('activity_create_table.sql')


class Activity(AkoData):
    id = 0
    platform = ''
    source_url = ''
    created_at = 0
    title = ''
    description = ''
    thumbnail_url = ''
    tag = list()
    extra = dict

    def __init__(self):
        pass

