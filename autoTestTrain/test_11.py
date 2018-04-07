#coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import os.path

import MySQLdb

import logging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

db=MySQLdb.connect('localhost','root','123456','yuerData',charset='utf8')
cursor=db.cursor()

def checkname(name,pw):
    sql="select * from user where name='%s'" % name
    logging.info(sql)
    cursor.execute(sql)
    result=cursor.fetchall()
    logging.info(result)
    if len(result)==1 and result[0][2]==pw:
        return True
    else:
        logging.info('error')
        return False
def register(name,pw):
    sql="select * from user where name='%s'" % name
    logging.info(sql)
    cursor.execute(sql)
    result=cursor.fetchall()
    if len(result)==0:
        sql="insert * from user where name='%s'" % name
    else:
        return False


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

class WelcomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('index.html', user=self.current_user)

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html',error=None)
    def post(self):
        name=self.get_argument("username")
        pw=self.get_argument("password")
        logging.debug('please input name and pw')
        if checkname(name,pw):
            self.set_secure_cookie("username", name)
            self.set_secure_cookie("password", pw)
            logging.debug('登录成功.')
            self.redirect("/")
        else:
            self.render('login.html',error='登录失败')

class LogoutHandler(BaseHandler):
    def post(self):
        if (self.get_argument("logout", None)):
            self.clear_cookie("username")
        self.redirect("/")

class registerHandler(BaseHandler):
    def get(self):
        self.render('register.html',error=None)

    def post(self):
        name=self.get_argument("username")
        pw1=self.get_argument("password1")
        pw2=self.get_argument("password1")
        if pw1!=pw2:
            self.render('register.html',error='两次密码不一致')
        else:
            self.redirect("/login.html")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    settings = {
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        "login_url": "/login"
    }
    application = tornado.web.Application([
        (r'/', WelcomeHandler),
        (r'/login', LoginHandler),
        (r'/logout', LogoutHandler),
        (r'/register', registerHandler)
    ],debug= True,**settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()