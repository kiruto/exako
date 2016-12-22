# -*- coding: utf-8 -*-
import os
import subprocess
import sys

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

import admin
import config
import sql_alchemy
from application import app
from environment import get_dir

import routing
from runtime_context import init_runtime_context
from sql_alchemy import event_listeners


def start_service():
    # app.run(host="0.0.0.0", port=80)
    sql_alchemy.db.init_app(app)
    event_listeners.init_listeners()
    with app.app_context():
        init_runtime_context()
    admin.init_console(app, sql_alchemy.db)
    routing.init_app(app)

    http_server = HTTPServer(WSGIContainer(app))
    http_server.bind(config.HTTP_PORT)
    http_server.start(0)
    IOLoop.instance().start()


def update_proto_files():
    sql_file_path = get_dir('database')
    sql_list = os.listdir(sql_file_path)
    for i in sql_list:
        if os.path.splitext(i)[1] == '.sql':
            p = subprocess.Popen(['sql-protobuf', i], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                print(line)
            retval = p.wait()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        start_service()
    elif sys.argv[1] == 'proto':
        update_proto_files()
