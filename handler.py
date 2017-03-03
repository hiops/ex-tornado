# coding: utf-8

import logging

import tornado.web
import tornado.escape

from models import DB_Session,User


RES_CODE_SUCCESS = 0
RES_CODE_PARAMETER_MISSED = 254
RES_CODE_UNKNOWN_ERROR = 255


def requires(*args):
    """装饰器：必选参数（以JSON格式），缺失返回254"""

    def dec(func):
        def wrapper(self):
            self.parameters = tornado.escape.json_decode(self.request.body)
            for key in args:
                if key not in self.parameters:
                    self.make_response(res_code=RES_CODE_PARAMETER_MISSED)
            func(self)

        return wrapper

    return dec


def log_data(func):
    """装饰器：将请求和返回的值打印到日志"""

    def wrapper(self):
        logging.info(
            '`'.join([str(arg) if arg is not None else '' for arg in ('req', self.request.uri, self.request.body)]))
        func(self)
        logging.info(
            '`'.join([str(arg) if arg is not None else '' for arg in ('req', self.request.uri, self.response)]))

    return wrapper


def handle_exception(func):
    """装饰器：捕捉异常，返回255"""

    def wrapper(self):
        try:
            func(self)
        except Exception, e:
            logging.exception(e)
            self.make_response(res_code=RES_CODE_UNKNOWN_ERROR)

    return wrapper


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.dbsession = DB_Session()

    def on_finish(self):
        self.dbsession.close()

    def get_current_user(self):
        return self.get_secure_cookie("username")


class TestHandler(BaseHandler):
    def get(self):
        self.write('hello world')
class GetUserByIdHandler(BaseHandler):
    def get(self,user_id):
        user = self.dbsession.query(User).filter(User.user_id==user_id).all()
        self.write(user[0].username)


class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user = self.dbsession.query(User).filter(User.username==username).first()
        if user != None and user.check_password_hash(password):
            print user.password
            self.set_secure_cookie("username", self.get_argument("username"))
            self.redirect("/")
        else:
            self.write("username or password error !")

class WelcomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('index.html', user=self.current_user)

class LogoutHandler(BaseHandler):
    def get(self):
        if (self.get_argument("logout", None)):
            self.clear_cookie("username")
            self.redirect("/")


urls=[
    (r'/', WelcomeHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/test',TestHandler),
    (r'/user/([0-9]+)',GetUserByIdHandler),
]
