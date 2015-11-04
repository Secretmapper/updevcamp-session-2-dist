#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

from lib import helpers

print(helpers.render('header', {'title': "MVC"}))
print('''
    <p>MVC</p>
    <p>This is the article for MVC</p>
''')
print(helpers.render('footer'))
