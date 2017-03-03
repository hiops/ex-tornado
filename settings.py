#!/usr/bin/env python
# coding: utf-8

import os
from os import environ
debug = True
template_path = os.path.join(os.path.dirname("__file__"), "templates")
static_path = os.path.join(os.path.dirname("__file__"), "static")
xsrf_cookies = True
login_url = "/login"
cookie_secret = "dskfhisdjklagkfdklag;lkjasdklgjkldsjaklgjkldsfksdklf"
autoescape = None
##template_loader=utils.ZipLoader
gzip=True
static_url_prefix = "/static/"
##static_handler_class = MyStaticFileHandler
##static_handler_args = { "key1":"value1", "key2":"value2"  }
##log_function = your_fun

DBINFO = {
    'product':{
        'db_name' : 'test',
        'db_user' : 'test',
        'db_passwd' : 'test',
        'db_host' : '127.0.0.1',
        'db_port' : 3306
    },
    'develop':{
        'db_name' : 'test',
        'db_user' : 'root',
        'db_passwd' : '',
        'db_host' : '127.0.0.1',
        'db_port' : 3306
    }
}

if debug:
    dbenv = "develop"
else:
    dbenv = "product"

DB_CONFIG = 'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % (DBINFO[dbenv]['db_user'], DBINFO[dbenv]['db_passwd'], DBINFO[dbenv]['db_host'], DBINFO[dbenv]['db_port'], DBINFO[dbenv]['db_name'])

SECRET_KEY='aaaaaaaaaaaaa'
PASSWD_SALT='sec string'
