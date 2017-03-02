#!/usr/bin/env python
# coding: utf-8

import os
import tornado.web
from tornado.options import define, options
import settings

from handler import *

def app():
    #setting = {
    #    'cookie_secret': 'D8888888888kasdfFKwlwfsdfsa1204mx',
    #    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    #    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    #    'debug': True,
    #}
    setting = options.as_dict()
    tapp = tornado.web.Application(
        handlers=[
            (r"/static/(.*)", tornado.web.StaticFileHandler),
            # dict(path=settings.static_path, "static"),
            #('.*', tornado.web.FallbackHandler, dict(fallback=container)),
        ], **setting)
    tapp.add_handlers(".*$",urls)
    return tapp
