# -*- coding: utf-8 -*-

import database
from sql_alchemy import db


def create_table(file_name: str):
    def _decorator(cls):
        database.exec_sql_file(file_name)
        return cls
    return _decorator


@create_table('activity_create_table.sql')
class AkoActivity(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    platform = db.Column('platform', db.String)
    source_url = db.Column('source_url', db.Text)
    create_at = db.Column('create_at', db.TIMESTAMP)
    title = db.Column('title', db.Text)
    description = db.Column('description', db.Text)
    thumbnail_url = db.Column('thumbnail_url', db.Text)
    tag = db.Column('tag', db.String)
    extra = db.Column('extra', db.Text)


@create_table('lang_create_table.sql')
class AkoLang(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(20), unique=True, nullable=False)

    def __str__(self):
        return self.name


@create_table('meta_create_table.sql')
class AkoSiteMeta(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(60), nullable=False)
    value = db.Column('value', db.Text)
    lang_id = db.Column('lang', db.Integer, db.ForeignKey(AkoLang.id), nullable=False)
    lang = db.relationship(AkoLang)


@create_table('settings_create_table.sql')
class AkoSettings(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(255), nullable=False)
    value = db.Column('value', db.Text)
    comment = db.Column('comment', db.Text)

