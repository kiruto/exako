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
import swagger
from application import app
from environment import get_dir

import routing
from repo import web_dist
from runtime_context import init_runtime_context
from sql_alchemy import event_listeners


def init():
    web_dist.check_git_repo()
    sql_alchemy.db.init_app(app)
    event_listeners.init_listeners()
    with app.app_context():
        init_runtime_context()
    admin.init_console(app, sql_alchemy.db)
    swagger.init_connexion(app)
    routing.init_app(app)
    return app


def start_service(debug=False):
    init()
    if debug:
        app.run(host="0.0.0.0", port=config.HTTP_PORT)
    else:
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
    elif sys.argv[1] == 'debug':
        start_service(True)
