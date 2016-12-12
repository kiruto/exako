# -*- coding: utf-8 -*-
import MySQLdb as MariaDB
from common import print_stack_trace

import config
from src import environment

maria_db_connection = MariaDB.connect(user=config.MARIA_USER,
                                      password=config.MARIA_PASSWORD,
                                      database=config.MARIA_DATABASE)
cursor = maria_db_connection.cursor()


def exec_sql_file(*file_path: str):
    path = environment.get_file('database', *file_path)
    file = open(path, 'r')
    sql = file.read()
    file.close()
    commands = sql.split(';')
    for cmd in commands:
        if not cmd:
            continue
        try:
            cursor.execute(cmd)
        except MariaDB.OperationalError as msg:
            print_stack_trace()
            print('skipped: %s \n %s' % (msg, cmd))


def exec_query(query: str, args: list=None):
    result = cursor.execute(query, args)
    if not result:
        return None
    elif len(result) == 1:
        return result[0]
    else:
        return result


def exec_many(query: str, args: list):
    result = cursor.executemany(query, args)
    if not result:
        return None
    elif len(result) == 1:
        return result[0]
    else:
        return result


def search_one_or_none(query: str, args: list=None):
    result = exec_query(query, args)
    return None if not result else result[0]
