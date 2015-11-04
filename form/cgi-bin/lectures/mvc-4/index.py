#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

from lib import helpers

print(helpers.render('header', {'title': "UP DevCamp"}))
print(helpers.render('home'))
print(helpers.render('footer'))
