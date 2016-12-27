# -*- coding: utf-8 -*-
import runtime_context
import sql_alchemy
from sql_alchemy import db
from sql_alchemy.databases import AkoArticle, AkoTag, AkoTagValue, AkoArticleContent


def article_meta_list_get(lang, tag=None, cat=None, page=None, lim=None):
    def get_struct():
        return {
            "id": 0,
            "category": "string",
            "tag": [
                "string"
            ],
            "img_url": "string",
            "img_type": 0,
            "url_title": "string",
            "description": "string"
        }
    result = list()
    page = 0 if not page else page
    lim = 20 if not lim else lim

    query = db.session.query(AkoArticle)

    if tag:
        query = query.filter(AkoArticle.tags.has(tag))
    if cat:
        query = query.filter(AkoArticle.cat_id == cat)
    items = query.limit(lim).offset(page * lim).all()
    for item in items:

        s = get_struct()
        s['id'] = item.id
        s['category'] = '' if not item.cat else item.cat.tag_content[0].name
        tags = list()

        s['tag'] = []
        s['img_url'] = ''
        result.append(s)
    return result


def article_get(lang, id) -> str:
    return 'do some magic!'
