# -*- coding: utf-8 -*-
from src import database


class AkoData:

    fields = None
    unique = None

    def __init__(self):
        self.table_name = ''
        pass

    @classmethod
    def create(cls, *args):
        pass

    @classmethod
    def batch_save(cls, lst):
        fields = str(cls.fields)
        field_stub = ','.join(['?'] * len(cls.fields))
        values = list(set(cls.fields) - set(cls.unique))
        value_stub = []
        for v in values:
            value_stub.append('%s = VALUES(%s)' % (v, v))
        value_stub = ','.join(value_stub)

        data_list = []
        for l in lst:
            data_list.append(l.to_tuple())

        query = """
        INSERT INTO userfan
            {fields}
        VALUES
            ({field_stubs})
        ON DUPLICATE KEY UPDATE
            {value_stub} ;
                   """.format(fields=fields, field_stubs=field_stub, value_stub=value_stub)
        database.exec_many(query, data_list)

    def save(self):
        pass

    def to_tuple(self):
        pass

    def map_field(self, fields):
        self.__class__.fields = fields

    def map_unique(self, fields):
        self.__class__.unique = fields

    @classmethod
    def find_one(cls, query: str, *args: str):
        if not args:
            args = None

        def decorator(fun):
            result = database.search_one_or_none(query, args)
            instance = fun(result)
            if isinstance(instance, cls):
                return instance
            else:
                return cls.create(result)
        return decorator

    @classmethod
    def for_all(cls, query: str, *args: str):
        if not args:
            args = None

        def decorator(fun):
            result = database.exec_query(query, args)
            result_list = list()
            if isinstance(result, list):
                for r in result:
                    instance = fun(r)
                    if isinstance(instance, cls):
                        result_list.append(instance)
                    else:
                        result_list.append(cls.create(r))
            return result_list
        return decorator


def table_file():
    pass
