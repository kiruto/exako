# -*- coding: utf-8 -*-
from sqlalchemy import desc
from sqlalchemy.orm import joinedload

import runtime_context
import sql_alchemy
from sql_alchemy import db
from sql_alchemy.databases import AkoArticle, AkoTag, AkoTagValue, AkoArticleContent


def article_meta_list_get(lang, tag=None, cat=None, page=0, lim=20):
    if page < 0 or lim < 0:
        return []

    def get_struct():
        return {
            "id": 0,
            "category": "string",
            "tag": [
                "string"
            ],
            "img_url": "string",
            "img_type": 0,
            "title": "string",
            "description": "string"
        }
    result = list()
    language = runtime_context.lang(lang)
    query = db.session.query(AkoArticle)

    if tag:
        t = runtime_context.find_tag(tag, language)
        if not t:
            return []
        query = query.filter(AkoArticle.tags.any(t.id == AkoTag.id))
    if cat:
        c = runtime_context.find_tag(cat, language)
        if not c:
            return []
        query = query.filter(AkoArticle.cat_id == c.id)
    items = query.order_by(desc(AkoArticle.created_at)).limit(lim).offset(page * lim).all()
    for item in items:
        s = get_struct()
        s['id'] = item.id
        s['category'] = '' if not item.cat else item.cat.tag_content[0].name
        tags = list()
        for t in item.tags:
            tags.append(sql_alchemy.filter_lang_id(t.tag_content, language.id).name)
            continue
        s['tag'] = tags
        s['img_url'] = ''
        for e in item.extra:
            if e.prop.name == 'cover_type':
                s['img_type'] = e.val
                break
        c = sql_alchemy.filter_lang_id(item.content, language.id)
        s['description'] = c.description
        s['title'] = c.title
        result.append(s)
    return result


def article_get(lang, id) -> str:
    return 'do some magic!'
