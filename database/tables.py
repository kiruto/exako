# -*- coding: utf-8 -*-
import database


class Tables:

    _table_dict = dict()

    def __init__(self):
        pass

    def table(self, fun, name: str, file: str):
        database.exec_sql_file(file)

        def decorator():
            instance = fun()
            self._table_dict[name] = instance.__class__
            return instance
        return decorator

    def field(self, fun, field):
        def decorator():
            pass


tables = Tables()
