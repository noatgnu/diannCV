import sys

import tornado.httpserver
from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler
from tornado.options import define, options
import asyncio

from diannCV.handlers import MainHandler, WebSocketComm, GetIDHandler, ProcessFileHandler

define("port", default=8000, help="Port number")


analysis_cache = {}

if sys.platform.startswith("win32"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    app.add_handlers(
        r'(localhost|127\.0\.0\.1|adept\.proteo\.info|10\.202\.62\.27)',
        [
            (r"/", MainHandler),
            (r"/rpc", WebSocketComm),
            (r"/getID", GetIDHandler),
            (r"/processFile", ProcessFileHandler),
            (r"/static", StaticFileHandler, dict(path="static"))
        ]
    )
    server = tornado.httpserver.HTTPServer(app)
    server.bind(options.port)
    server.start(1)
    IOLoop.current().start()