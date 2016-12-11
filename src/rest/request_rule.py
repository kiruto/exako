# -*- coding: utf-8 -*-
from flask import request
from protobuf import Request

import common

GET = 'GET'
POST = 'POST'
DELETE = 'DELETE'

ACTION_SELECT = Request.Action.SELECT
ACTION_INSERT = Request.Action.INSERT
ACTION_UPDATE = Request.Action.UPDATE
ACTION_DELETE = Request.Action.DELETE

ACCEPT_METHODS = (GET, POST, DELETE)
ACCEPT_ACTIONS = (ACTION_SELECT, ACTION_INSERT, ACTION_UPDATE, ACTION_DELETE)


def accept(args: Request) -> bool:
    check, msg = check_method()
    if not check:
        common.debug_info(msg)
        return False
    check, msg = check_action(args)
    if not check:
        common.debug_info(msg)
        return False


def check_method() -> (False, 'method HEAD denied'):
    method = request.method
    return (True, 'method ok') if method in ACCEPT_METHODS else (False, 'method %s denied' % method)


def check_action(args: Request) -> (False, 'action XXX denied'):
    if not args.HasField('action'):
        return False, 'no action'
    action = args.action
    if not action or action not in ACCEPT_ACTIONS:
        return False, 'action %s denied' % action
    return True, 'action ok'
