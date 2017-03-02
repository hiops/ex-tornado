# coding: utf-8

import os
import logging

import tornado.wsgi

from settings import cookie_secret
from handler import *

metadata = dict(
    static_path=os.path.join(os.path.dirname(__file__), 'static'),
    template_path=(os.path.join(os.path.dirname(__file__), "templates")),
    cookie_secret=cookie_secret,
)

urls = [
    (r'/test', TestHandler),
]


class XApplication(tornado.wsgi.WSGIApplication):
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        tornado.wsgi.WSGIApplication.__init__(self, urls, **metadata)
