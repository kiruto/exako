# -*- coding: utf-8 -*-
import database
from database.ako_data import AkoData

database.exec_sql_file('user_create_table.sql')


class User(AkoData):
    uid = 0
    create_at = 0
    name = ''
    password = ''
    mail = ''
    extra = {}

    def __init__(self, *args):
        super().__init__()

    def save(self):
        if self.uid:
            insert_data = (self.uid, self.name, self.password, self.mail, self.extra)
            database.cursor.execute(
                'REPLACE into exako.user(uid, name, password, mail, extra)VALUE(?, ?, ?, ?, ?)',
                insert_data)
        else:
            insert_data = (self.name, self.password, self.mail, self.extra)
            database.cursor.execute(
                'INSERT into exako.user(name, password, mail, extra)VALUE(?, ?, ?, ?)',
                insert_data)


def find_user_by_uid(uid: str) -> User:
    result = database.cursor.execute('SELECT * FROM exako.user WHERE uid=?', [uid])
    return User(*result)


def find_user_by_mail(mail: str) -> User:
    result = database.cursor.execute('SELECT * FROM exako.user WHERE mail=?', [mail])
    return User(*result)
