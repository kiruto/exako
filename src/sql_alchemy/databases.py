# -*- coding: utf-8 -*-
from sql_alchemy import db, create_table


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
    meta_list = db.relationship('AkoMetaValue', backref='lang', lazy='dynamic')
    tag_list = db.relationship('AkoTagValue', backref='lang', lazy='dynamic')
    article_content_list = db.relationship('AkoArticleContent', backref='lang', lazy='dynamic')

    def __str__(self):
        return self.name


@create_table('meta_create_table.sql')
class AkoSiteMeta(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(60), nullable=False)
    comment = db.Column('comment', db.Text)
    value = db.relationship('AkoMetaValue', backref='meta_info')

    def __str__(self):
        return '%s: %s' % (self.name, self.comment)


@create_table('meta_value_create_table.sql')
class AkoMetaValue(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    meta_id = db.Column('key_name', db.Integer, db.ForeignKey(AkoSiteMeta.id), nullable=False)
    lang_id = db.Column('lang', db.Integer, db.ForeignKey(AkoLang.id), nullable=False)
    value = db.Column('value', db.Text)


@create_table('settings_create_table.sql')
class AkoSettings(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(255), nullable=False)
    value = db.Column('value', db.Text)
    comment = db.Column('comment', db.Text)


@create_table('image_create_table.sql')
class AkoImage(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(255), nullable=False)
    path = db.Column('path', db.String(255))
    url = db.Column('url', db.String(255))
    created_at = db.Column('created_at', db.TIMESTAMP)

    def __str__(self):
        return '%s: path:%s'


@create_table('tag_create_table.sql')
class AkoTag(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    extra = db.Column('extra', db.Text)
    tag_content = db.relationship('AkoTagValue', backref='tag')

    def __str__(self):
        return self.extra


@create_table('tag_value_create_table.sql')
class AkoTagValue(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    tag_id = db.Column('tag', db.Integer, db.ForeignKey(AkoTag.id), nullable=False)
    lang_id = db.Column('lang', db.Integer, db.ForeignKey(AkoLang.id))
    name = db.Column('name', db.String(255))


# M2M table
article_tag_table = db.Table('ako_m2m_article_tag', db.Model.metadata,
                             db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                             db.Column('article', db.Integer, db.ForeignKey('ako_article.id')),
                             db.Column('tag', db.Integer, db.ForeignKey('ako_tag.id')))


article_image_table = db.Table('ako_m2m_article_image', db.Model.metadata,
                               db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                               db.Column('article', db.Integer, db.ForeignKey('ako_article.id')),
                               db.Column('image', db.Integer, db.ForeignKey('ako_image.id')))


@create_table('article_create_table.sql')
class AkoArticle(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    tags = db.relationship('AkoTag', secondary=article_tag_table)
    cat_id = db.Column('cat', db.Integer, db.ForeignKey(AkoTag.id))
    images = db.relationship('AkoImage', secondary=article_image_table)
    content = db.relationship('AkoArticleContent', backref='article')
    created_at = db.Column('created_at', db.TIMESTAMP)


@create_table('article_content_create_table.sql')
class AkoArticleContent(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    article_id = db.Column('article', db.Integer, db.ForeignKey(AkoArticle.id), nullable=False)
    lang_id = db.Column('lang', db.Integer, db.ForeignKey(AkoLang.id), nullable=False)
    title = db.Column('title', db.Text)
    description = db.Column('description', db.Text)
    content = db.Column('content', db.Text)

    def __str__(self):
        return self.title
