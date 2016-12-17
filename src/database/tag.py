# -*- coding: utf-8 -*-
import database
from database.tables import tables

from database.ako_data import AkoData


class Tag(AkoData):

    @tables.src(name='ako_tag', file='tag_create_table.sql')
    def __init__(self):
        super().__init__()
