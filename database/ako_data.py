# -*- coding: utf-8 -*-
import database


class AkoData:

    def __init__(self):
        pass

    @classmethod
    def create(cls, *args) -> database.AkoData:
        return None

    @classmethod
    def find_one(cls, fun, query: str, *args: str):
        if not args:
            args = None

        def decorator(stub=None):
            result = stub if stub else database.search_one_or_none(query, args)
            instance = fun(result)
            if isinstance(instance, cls):
                return instance
            else:
                return cls.create(result)
        return decorator

    @classmethod
    def for_all(cls, fun, query: str, *args: str):
        if not args:
            args = None

        def decorator(stub=None):
            result = stub if stub else database.exec_query(query, args)
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
