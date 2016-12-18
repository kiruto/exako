# -*- coding: utf-8 -*-
from protobuf import rest_request_pb2


def parse_buf(obj, **kwargs):
    for arg in kwargs:
        obj.__setattr__(arg, kwargs[arg])
    return obj


def proto_response(contents, result=None, code=1, msg='ok'):
    response = rest_request_pb2.Response()
    response.code = code
    response.msg = msg
    if result:
        response.result = result
    if contents:
        for arg in contents:
            buf = response.content.add()
            buf.Pack(arg)
    return response.SerializeToString()
