# -*- coding: utf-8 -*-
from flask_admin.contrib import sqla

from sql_alchemy.databases import AkoMetaValue


class CommonDatabase(sqla.ModelView):
    pass


class MetaDatabase(sqla.ModelView):
    inline_models = (AkoMetaValue, )


class LangDatabase(sqla.ModelView):
    inline_models = (AkoMetaValue, )
