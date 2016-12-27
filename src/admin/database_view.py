# -*- coding: utf-8 -*-
import os.path as op

import time
from flask_admin import form
from flask_admin.actions import action
from flask_admin.contrib import sqla
from markupsafe import Markup
from werkzeug.utils import secure_filename

from environment import get_image_upload_path, get_abs_image_upload_path, get_raw_image_url
from repo import web_dist
from sql_alchemy.databases import AkoMetaValue, AkoArticleContent, AkoTag, AkoTagValue, AkoImage


class CommonDatabase(sqla.ModelView):
    create_modal = True
    edit_modal = True


class MetaDatabase(sqla.ModelView):
    inline_models = (AkoMetaValue, )
    column_filters = ['name', 'comment']
    column_searchable_list = ['name', 'comment']
    column_editable_list = ['name', 'comment']
    create_modal = True
    edit_modal = True


class LangDatabase(sqla.ModelView):
    create_modal = True
    edit_modal = True
    form_excluded_columns = ['meta_list', 'tag_list', 'article_content_list']


class ImageFileDatabase(sqla.ModelView):

    def _prefix_name(self, obj, file_data):
        p0, p1 = op.splitext(file_data.filename)
        p2 = time.strftime('%Y_%m_%d-%H_%M_%S', time.localtime(time.time()))
        return secure_filename('%s-%s%s' % (p2, p0, p1))

    def _list_thumbnail(self, context, model, name):
        return Markup('<img src="%s" style="max-width:100px;max-height:100px;width:auto;height:auto">' %
                      get_raw_image_url(model))

    column_formatters = {
        'path': _list_thumbnail
    }

    form_excluded_columns = ['created_at', 'url']
    form_extra_fields = ''
    form_overrides = {
        'path': form.fields.fields.HiddenField,
        'name': form.FileUploadField,
        'url': form.fields.fields.HiddenField,
    }
    form_args = {
        'path': {
            'default': get_image_upload_path()
        },
        'name': {
            'label': 'File',
            'base_path': get_abs_image_upload_path(),
            'allow_overwrite': False,
            'namegen': _prefix_name
        }
    }

    create_modal = True
    edit_modal = True

    @action('sync git', 'push origin to remote')
    def sync_git(self, *args, **kwargs):
        web_dist.push()


class ArticleDatabase(sqla.ModelView):
    inline_models = (AkoArticleContent, )
    form_excluded_columns = ['created_at', ]

    def _list_article_name(self, context, model, name):
        if model.content:
            return model.content[0].title
        else:
            return 'empty'

    def _list_article_copies(self, context, model, name):
        if model.content:
            return ','.join(x.lang for x in model.content)
        else:
            return 'none'

    column_formatters = {
        'title': _list_article_name,
        'copies': _list_article_copies
    }

    def get_column_names(self, only_columns, excluded_columns):
        only_columns += ['title', 'copies']
        return super().get_column_names(only_columns, excluded_columns)


class TagDatabase(sqla.ModelView):
    inline_models = (AkoTagValue, )
    form_excluded_columns = ['article_cat_list']

    def _list_tag_sample(self, context, model, name):
        return model.extra if model.extra else model.__str__()

    column_formatters = {
        'sample': _list_tag_sample
    }
    column_editable_list = ['extra']

    def get_column_names(self, only_columns, excluded_columns):
        only_columns += ['sample']
        return super().get_column_names(only_columns, excluded_columns)
