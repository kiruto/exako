# -*- coding: utf-8 -*-
from exceptions import XakoException, XakoLangException
from sql_alchemy.databases import AkoLang, AkoTag

langs = None
tags = None


def init_runtime_context():
    global langs, tags
    langs = AkoLang.query.all()
    tags = AkoTag.query.all()


def lang(name):
    global langs
    for l in langs:
        if l.name == name:
            return l
    raise XakoLangException()


def find_tag(name, language):
    global tags
    if not language:
        l = None
    elif isinstance(language, str):
        l = lang(language)
    elif isinstance(language, AkoLang):
        l = language
    else:
        l = None
    for tag in tags:
        for t in tag.tag_content:
            if l and t.lang_id != l.id:
                continue
            if name == t.name:
                return tag
