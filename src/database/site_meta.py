# -*- coding: utf-8 -*-
import database
from database.ako_data import AkoData
from database.tables import tables

meta_dict = {}


class SiteMeta(AkoData):

    @tables.src(name='ako_meta',
                file='meta_create_table.sql',
                field=['ako_meta', 'name', 'value', 'lang'],
                unique=['id', 'name'])
    def __init__(self):
        super().__init__()
        self.name = ''
        self.value = ''
        self.lang = ''

    @classmethod
    def create(cls, *args):
        meta = SiteMeta()
        meta.name = args[1]
        meta.value = args[2]
        meta.lang = args[3]
        return meta

    def to_tuple(self):
        return self.name, self.value, self.lang


@SiteMeta.for_all('SELECT * FROM ako_meta')
def get_all_meta(meta_raw):
    return SiteMeta.create(meta_raw)


def add_to_dict(meta: list):
    global meta_dict
    for m in meta:
        meta_dict[m.name] = m


def batch_save():
    SiteMeta.batch_save(list(meta_dict.values()))
