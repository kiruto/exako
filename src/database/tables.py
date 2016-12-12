# -*- coding: utf-8 -*-
import environment
from environment import get_file
from src import database


class Tables:

    _table_dict = dict()

    def __init__(self):
        pass

    def src(self,
            name: str,
            file: str,
            path: str=environment.SQL,
            field: list=None,
            unique: list=None):

        database.exec_sql_file(get_file(path, file))

        def decorator(fun):
            instance = fun()
            instance.table_name = name
            self._table_dict[name] = instance.__class__

            if field:
                instance.__class__.map_field(field)
            if unique:
                instance.__class__.map_unique(unique)

            return instance
        return decorator


tables = Tables()
