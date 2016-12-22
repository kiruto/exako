# -*- coding: utf-8 -*-
import os.path as op

import time
from flask_admin import form
from flask_admin.contrib import sqla
from werkzeug.utils import secure_filename

from environment import get_image_upload_path
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


def prefix_name(obj, file_data):
    p0, p1 = op.splitext(file_data.filename)
    p2 = time.strftime('%Y_%m_%d-%H_%M_%S', time.localtime(time.time()))
    return secure_filename('%s-%s%s' % (p2, p0, p1))


class ImageFileDatabase(sqla.ModelView):

    form_extra_fields = ''
    form_overrides = {
        'path': form.fields.fields.HiddenField,
        'name': form.FileUploadField
    }

    form_args = {
        'path': {
            'default': get_image_upload_path()
        },
        'name': {
            'label': 'File',
            'base_path': get_image_upload_path(),
            'allow_overwrite': False,
            'namegen': prefix_name
        }
    }
