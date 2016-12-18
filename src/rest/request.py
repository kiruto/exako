# -*- coding: utf-8 -*-
from protobuf import rest_request_pb2


def parse_request_dict(req: rest_request_pb2.Request):
    if not req.HasField('kwargs'):
        return None
    result = dict()
    for k in req.kwargs:
        result[k.key] = k.value
    return result
