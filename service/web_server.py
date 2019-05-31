# -*- UTF-8 -*-
# -*- UTF-8 -*-
from tornado.escape import json_encode
from tornado.web import RequestHandler
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
import regex as re
import json

from entity.post import PostJSONEncoder
from entity.query import Query

define("port", default=8890, help="run on the given port", type=int)


class SearchHandler(RequestHandler):

    def prepare(self):
        pass

    def get(self):
        title = self.get_query_argument('title', default='')
        body = self.get_query_argument('body', default='')
        created_date = self.get_query_argument('created_date', default='')
        tags = self.get_query_argument('tags', default='')
        tag_list = re.findall('(\<[^ \>]+\>)', tags)
        size = self.get_query_argument('size', default=10)

        query = Query(title=title, body=body,
                      tag_list=tag_list, created_date=created_date)
        query.search(size=size)
        query.arrange()
        post_results = query.get_results()
        results = json.dumps(post_results, cls=PostJSONEncoder)
        self.set_header('Content-type', 'application/json')
        self.write(results)

    def post(self):
        self.get()

    def on_finish(self):
        pass


def run_server():
    app = Application([
        (r"/search", SearchHandler)
    ])
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.current().start()


if __name__ == '__main__':
    run_server()
