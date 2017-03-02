# coding: utf-8

from os import environ

SECRET_KEY='aaaaaaaaaaaaa'

debug = True

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

db_config = 'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % (DBINFO[dbenv]['db_user'], DBINFO[dbenv]['db_passwd'], DBINFO[dbenv]['db_host'], DBINFO[dbenv]['db_port'], DBINFO[dbenv]['db_name'])
print db_config
# cookie加密的密钥
cookie_secret = 'test' if debug else SECRET_KEY
