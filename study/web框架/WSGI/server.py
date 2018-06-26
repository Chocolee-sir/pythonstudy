#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Chocolee'

from wsgiref.simple_server import make_server
import time



def foo_lee(req):
    f = open("index_lee.html", "rb")
    data = f.read()
    return data


def login(req):
    pass



def signup(req):
    pass


def show_time(req):
    times = time.ctime()
    # return ("<h1>时间：%s</h1>"%(str(times))).encode("utf8")
    f = open("showtime.html", "rb")
    data = f.read().decode("utf8").replace("@time@", times)
    return data.encode("utf8")



def router():
    url_patterns = [
        ("/login", login),
        ("/signup", signup),
        ("/lee", foo_lee),
        ("/showtime", show_time)
    ]
    return url_patterns


def application(environ, start_response):

    start_response('200 OK', [('Content-Type', 'text/html')])

    # print("path",environ["PATH_INFO"])
    path = environ["PATH_INFO"]
    # if path == "/alex":
    #     return [b'<h1>Hello,alex</h1>']
    # elif path == "/lee":
    #     return [foo_lee(11)]
    # else:
    #     return [b'<h1>404</h1>']

    url_patterns = router()
    func = None
    for item in url_patterns:
        if item[0] == path:
            func = item[1]
            break

    if func:
        return [func(environ)]
    else:
        return [b'<h1>404</h1>']





httpd = make_server('0.0.0.0', 8080, application)

print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()