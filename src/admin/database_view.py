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
from sql_alchemy.databases import AkoMetaValue


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
    inline_models = (AkoMetaValue, )
    create_modal = True
    edit_modal = True


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
