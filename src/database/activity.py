# -*- coding: utf-8 -*-
from database.tables import tables

from src.database.ako_data import AkoData


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

    @tables.table(name='ako_activity', file='activity_create_table.sql')
    def __init__(self):
        super().__init__()
