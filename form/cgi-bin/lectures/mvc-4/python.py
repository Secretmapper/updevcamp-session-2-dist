#!/usr/local/bin/python3
import cgi
print("Content-type: text/html")

from lib import helpers

print(helpers.render('header', {'title': "Python"}))
print('''
    <p>Python</p>
    <p>This is the article for Python</p>
''')
print(helpers.render('footer'))
