# -*- coding: utf-8 -*-
import os

import subprocess
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

import admin
import config
import sql_alchemy
import swagger
from application import application
from environment import get_dir

import routing
from repo import web_dist
from runtime_context import init_runtime_context


class Serv:
    
    def __init__(self, *args):
        self.app = application()
        self.args = args

    def init(self):
        from sql_alchemy import event_listeners

        web_dist.check_git_repo()
        sql_alchemy.db.init_app(self.app)
        event_listeners.init_listeners()
        with self.app.app_context():
            init_runtime_context()
        admin.init_console(self.app, sql_alchemy.db)
        swagger.init_connexion(self.app)
        routing.init_app(self.app)
        return self.app

    def start_service(self, debug=False):
        self.init()
        if debug:
            self.app.run(host="0.0.0.0", port=config.HTTP_PORT)
        else:
            http_server = HTTPServer(WSGIContainer(self.app))
            http_server.bind(config.HTTP_PORT)
            http_server.start(0)
            IOLoop.instance().start()

    @classmethod
    def update_proto_files(cls):
        sql_file_path = get_dir('database')
        sql_list = os.listdir(sql_file_path)
        for i in sql_list:
            if os.path.splitext(i)[1] == '.sql':
                p = subprocess.Popen(['sql-protobuf', i], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for line in p.stdout.readlines():
                    print(line)
                retval = p.wait()

    def start(self):
        if self.args[0] == 'serv':
            self.start_service()
        elif self.args[0] == 'proto':
            self.update_proto_files()
        elif self.args[0] == 'debug':
            config.DEBUG = True
            self.start_service(True)
        else:
            print('Unknown argument: %s' % self.args[1])
