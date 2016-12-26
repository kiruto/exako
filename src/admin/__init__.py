# -*- coding: utf-8 -*-
import flask_admin as admin

from admin.database_view import CommonDatabase, MetaDatabase, LangDatabase, ImageFileDatabase, ArticleDatabase, \
    TagDatabase
from sql_alchemy.databases import AkoSiteMeta, AkoLang, AkoSettings, AkoImage, AkoArticle, AkoTag


class Cats:
    databases = 'Databases'


def init_console(app, db):
    console = admin.Admin(app, name='Console', template_mode='bootstrap3')
    console.add_view(
        MetaDatabase(AkoSiteMeta, db.session, category=Cats.databases)
    )
    console.add_view(
        LangDatabase(AkoLang, db.session, category=Cats.databases)
    )
    console.add_view(
        CommonDatabase(AkoSettings, db.session, category=Cats.databases)
    )
    console.add_view(
        ImageFileDatabase(AkoImage, db.session, category=Cats.databases)
    )
    console.add_view(
        ArticleDatabase(AkoArticle, db.session, category=Cats.databases)
    )
    console.add_view(
        TagDatabase(AkoTag, db.session, category=Cats.databases)
    )
