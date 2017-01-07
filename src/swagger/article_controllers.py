# -*- coding: utf-8 -*-
import re

from sqlalchemy import desc

import runtime_context
import sql_alchemy
from sql_alchemy import db
from sql_alchemy import rsp_check
from sql_alchemy.databases import AkoArticle, AkoTag, AkoTagValue, AkoArticleContent, AkoLang
from swagger.encrype import aes_dict
from swagger.rsp import error
img_re = re.compile('(<ako-img\[([0-9]*)\])', re.IGNORECASE)


def _parse_article_img(article_images, article_content):
    """
    Parse <ako-img[1956] height="14px" /> to <img src="http://some.img/url" height="14px" />
        by the image records in database
    :param article_images: AkoArticle.images
    :param article_content: AkoArticleContent.content
    :return: result
    """
    result = article_content
    result_array = img_re.findall(article_content)
    image_map = dict()
    for img in article_images:
        image_map[str(img.id)] = img
    for tup in result_array:
        # [('<ako-img[123]', '123'), ('<ako-img[1234]', '1234'), ('<ako-img[1235]', '1235'), ('<ako-img[1236]', '1236')]
        tag = tup[0]
        img = image_map[tup[1]]
        string = '<img src="%s" ' % img.get_url()
        result = result.replace(tag, string)
    return result


def _find_image_in_article(article, img_id):
    for img in article.images:
        if img.id == img_id:
            return img


def _fill_article_info(article: AkoArticle, language: AkoLang):
    struct = {
        "id": 0,
        "category": "string",
        "tag": [
            "string"
        ],
        "img_url": "string",
        "img_type": 0,
        "cover_name": None,
        "title": "string",
        "description": "string",
        "google_translation": False,
        "created_at": ""
    }
    s = struct
    s['id'] = article.id
    s['category'] = '' if not article.cat else sql_alchemy.filter_lang_id(article.cat.tag_content, language.id).name
    tags = list()
    for t in article.tags:
        tags.append(sql_alchemy.filter_lang_id(t.tag_content, language.id).name)
        continue
    s['tag'] = tags
    for e in article.extra:
        if e.prop.name == 'cover_type':
            s['img_type'] = int(e.val)
        if e.prop.name == 'cover_img':
            s['img_url'] = _find_image_in_article(article, int(e.val)).get_url()
        if e.prop.name == 'google_translate_%s' % language.name:
            s['google_translation'] = bool(e.val)
        if e.prop.name == 'cover_name_%s' % language.name:
            s['cover_name'] = e.val
    c = sql_alchemy.filter_lang_id(article.content, language.id)
    s['description'] = c.description
    s['title'] = c.title
    s['created_at'] = str(article.created_at)
    return s


@aes_dict
@rsp_check.lang
def article_meta_list_get(lang, tag=None, cat=None, page=0, lim=20):
    """
    List articles
    :param lang: language
    :param tag: tag name
    :param cat: category name
    :param page: page number starts by 0
    :param lim: items per page
    :return: List of following struct
    {
        "id": 0,
        "category": "string",
        "tag": [
            "string"
        ],
        "img_url": "string",
        "img_type": 0,
        "title": "string",
        "description": "string",
        "google_translation": bool,
        "created_at": "string"
    }
    """
    if page < 0 or lim < 0 or lim > 50:
        return error(40001, 'page or lim is not valid'), 400
    language = runtime_context.lang(lang)
    result = list()
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
        s = _fill_article_info(item, language)
        result.append(s)
    return result


@aes_dict
@rsp_check.lang
def article_get(lang, aid):
    """
    Get single article by id
    :param lang: language
    :param aid: Article record id
    :return:
    {
        "info": {
            "id": 0,
            "category": "",
            "tag": [],
            "img_url": "",
            "img_type": 0,
            "title": "",
            "description": ""
        },
        "content": ""
    }
    """
    language = runtime_context.lang(lang)
    item = db.session.query(AkoArticle).filter(AkoArticle.id == aid).one_or_none()
    if item:
        result = dict()
        result['info'] = _fill_article_info(item, language)
        content = sql_alchemy.filter_lang_id(item.content, language.id).content
        result['content'] = _parse_article_img(item.images, content)
        return result
    else:
        return {}
