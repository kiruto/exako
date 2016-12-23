# -*- coding: utf-8 -*-
import os
import os.path as op

from sqlalchemy import event

from environment import get_image_upload_path, STATIC_DIST_GIT_IMAGE_PATH
from sql_alchemy.databases import AkoImage


def init_listeners():

    @event.listens_for(AkoImage, 'after_insert')
    def _upload_image(mapper, connection, target):
        pass

    @event.listens_for(AkoImage, 'after_delete')
    def _delete_image(mapper, connection, target):
        if target.path:
            try:
                os.remove(op.join(STATIC_DIST_GIT_IMAGE_PATH, target.path, target.name))
            except OSError:
                # Don't care if was not deleted because it does not exist
                pass
