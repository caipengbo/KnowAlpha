# -*- UTF-8 -*-
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application

from service import config
from service.http_server import SearchHandler


def run_server():
    app = Application([
        (r"/search", SearchHandler)
    ])
    http_server = HTTPServer(app)
    http_server.listen(config.options['port'])
    print('Development server is running at http://10.1.1.32:%s/search' % config.options['port'])
    print('Notice: You can use parameters: title, body, created_date, tags, size')
    IOLoop.current().start()


if __name__ == '__main__':
    run_server()