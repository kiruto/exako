# -*- coding: utf-8 -*-
from database.tables import tables

from database.ako_data import AkoData


class Activity(AkoData):

    @tables.src(name='ako_activity', file='activity_create_table.sql')
    def __init__(self):
        super().__init__()
        self.id = 0
        self.platform = ''
        self.source_url = ''
        self.created_at = 0
        self.title = ''
        self.description = ''
        self.thumbnail_url = ''
        self.tag = list()
        self.extra = dict
