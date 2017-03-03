#!/usr/bin/env python
# coding: utf-8

import os
import tornado.web
from tornado.options import define, options
import settings
from settings import SESSION_OPTIONS

from handler import *

def make_app():
    setting = options.as_dict()
    tapp = tornado.web.Application(
        handlers=[
            (r"/static/(.*)", tornado.web.StaticFileHandler),
            # dict(path=settings.static_path, "static"),
            #('.*', tornado.web.FallbackHandler, dict(fallback=container)),
        ], **setting)
    tapp.add_handlers(".*$",urls)
    tapp.session_manager = session.SessionManager(SESSION_OPTIONS["session_secret"], SESSION_OPTIONS["session_store"], SESSION_OPTIONS["session_timeout"])
    return tapp
