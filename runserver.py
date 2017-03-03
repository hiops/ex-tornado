#!/usr/bin/env python
# coding: utf-8

import os
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

import app

define('port', default=8000, help='port', type=int)
define('host', default="0.0.0.0", help='host', type=str)
define('static_path', default=None, help='static_path', type=str)
define('template_path', default=None, help='template_path', type=str)
define('cookie_secret', default=None, help='cookie_secret', type=str)
define('login_url', default=None, help='login_url', type=str)
define('xsrf_cookies', default=None, help='xsrf_cookies', type=bool)
define('debug', default=True, help='debug level', type=bool)
options.parse_command_line()

config_file=os.path.join(os.path.dirname(__file__), "settings.py")
tornado.options.parse_config_file(config_file)
print options.as_dict()

def main():
    tornado_app = app.make_app()

    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port, options.host)

    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    print "Run server on %s:%s" % (options.host, options.port)
    main()
