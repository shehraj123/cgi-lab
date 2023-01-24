#!/usr/bin/env python3


import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import os
import secret
from http.cookies import SimpleCookie

s = cgi.FieldStorage()
username = s.getfirst('username')
password = s.getfirst('password')

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").get()

print("Content-Type: text/html")

if not username and not password:
    print(login_page())
elif username == secret.username and password== secret.password:
    print(secret_page(username, password))

else:
    print(login_page())
    print("username & password: ", username, password)