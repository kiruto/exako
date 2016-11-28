# -*- coding: utf-8 -*-
import MySQLdb as MariaDB

import config
import environment
from utils import print_stack_trace

maria_db_connection = MariaDB.connect(user=config.MARIA_USER,
                                      password=config.MARIA_PASSWORD,
                                      database=config.MARIA_DATABASE)
cursor = maria_db_connection.cursor()


def exec_sql_file(*file_path):
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
