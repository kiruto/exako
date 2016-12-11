# -*- coding: utf-8 -*-
import os
import sys

import subprocess
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

import config
from src.environment import get_dir
from src.application import app


def start_service():
    # app.run(host="0.0.0.0", port=80)
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(config.HTTP_PORT)
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
