# -*- coding: utf-8 -*-
from protobuf import Request


class QueryExecutor:

    def __init__(self, method: str, args: Request):
        self.method = method
        self.args = args
        self.query = ''

    def select_target(self):
        return '*' if not self.args.HasField('target') else self.args.target

    # Must be checked @ request_rule
    def data_source(self):
        return self.args.source

    # Must be checked @ request_rule
    def data_require(self):
        return self.args.require

    def select_query(self):
        self.query = 'SELECT ? FROM ? '
