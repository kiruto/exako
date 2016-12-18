# -*- coding: utf-8 -*-
from sql_alchemy.databases import AkoLang
langs = None


def init_runtime_context():
    global langs
    langs = AkoLang.query.all()
