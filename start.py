# -*- coding: utf-8 -*-
from application import app
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

import config

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=80)
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(config.HTTP_PORT)
    IOLoop.instance().start()
